from __future__ import annotations
import json
from pathlib import Path
from threading import Lock
from typing import Any
from flask import Flask, jsonify, request, send_from_directory
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "inventory_data.json"
app = Flask(__name__, static_folder=str(BASE_DIR), static_url_path="")
_DATA_LOCK = Lock()
def _normalize_id(value: Any) -> str:
    return str(value or "").strip().upper()
def _to_non_negative_number(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number < 0:
        return None
    return number
def _load_items() -> list[dict[str, Any]]:
    if not DATA_FILE.exists():
        return []
    try:
        # Use utf-8-sig so files saved with a UTF-8 BOM still parse correctly.
        with DATA_FILE.open("r", encoding="utf-8-sig") as file:
            payload = json.load(file)
    except (json.JSONDecodeError, OSError):
        return []
    if not isinstance(payload, list):
        return []
    items: list[dict[str, Any]] = []
    for index, raw in enumerate(payload, start=1):
        if not isinstance(raw, dict):
            continue
        item_id = _normalize_id(raw.get("id") or raw.get("item_id") or f"ITM{index:03d}")
        if not item_id:
            item_id = f"ITM{index:03d}"
        name = str(raw.get("name") or "Unnamed Item").strip()
        category = str(raw.get("category") or "Stationery").strip()
        quantity = int(_to_non_negative_number(raw.get("quantity")) or 0)
        price = _to_non_negative_number(raw.get("price")) or 0.0
        reorder = int(_to_non_negative_number(raw.get("reorder") or raw.get("reorder_level")) or 0)

        items.append(
            {
                "id": item_id,
                "name": name,
                "category": category,
                "quantity": quantity,
                "price": round(price, 2),
                "reorder": reorder,
            }
        )

    return items
def _save_items(items: list[dict[str, Any]]) -> None:
    payload: list[dict[str, Any]] = []
    for item in items:
        payload.append(
            {
                "item_id": item["id"],
                "name": item["name"],
                "category": item["category"],
                "quantity": item["quantity"],
                "price": item["price"],
                "reorder_level": item["reorder"],
            }
        )

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)
def _next_item_id(items: list[dict[str, Any]]) -> str:
    highest = 0
    for item in items:
        item_id = _normalize_id(item.get("id"))
        if item_id.startswith("ITM"):
            suffix = item_id.replace("ITM", "", 1)
            if suffix.isdigit():
                highest = max(highest, int(suffix))
    return f"ITM{highest + 1:03d}"
def _find_item_index(items: list[dict[str, Any]], item_id: str) -> int:
    normalized = _normalize_id(item_id)
    for index, item in enumerate(items):
        if _normalize_id(item.get("id")) == normalized:
            return index
    return -1
def _validate_item_payload(payload: dict[str, Any], existing_ids: set[str]) -> tuple[dict[str, Any] | None, str | None]:
    custom_id = _normalize_id(payload.get("id") or payload.get("item_id"))
    name = str(payload.get("name") or "").strip()
    category = str(payload.get("category") or "").strip()
    quantity = _to_non_negative_number(payload.get("quantity"))
    price = _to_non_negative_number(payload.get("price"))
    reorder = _to_non_negative_number(payload.get("reorder") or payload.get("reorder_level"))
    if not name:
        return None, "Item name is required."
    if not category:
        return None, "Category is required."
    if quantity is None or price is None or reorder is None:
        return None, "Quantity, price, and reorder must be non-negative numbers."
    if custom_id and custom_id in existing_ids:
        return None, "Item ID already exists."
    item = {
        "id": custom_id,
        "name": name,
        "category": category,
        "quantity": int(quantity),
        "price": round(price, 2),
        "reorder": int(reorder),
    }
    return item, None
@app.get("/")
def home() -> Any:
    return send_from_directory(BASE_DIR, "index.html")
@app.get("/api/items")
def get_items() -> Any:
    with _DATA_LOCK:
        items = _load_items()
    return jsonify({"items": items})
@app.post("/api/items")
def create_item() -> Any:
    payload = request.get_json(silent=True) or {}
    with _DATA_LOCK:
        items = _load_items()
        existing_ids = {_normalize_id(item.get("id")) for item in items}
        item_data, error = _validate_item_payload(payload, existing_ids)
        if error:
            return jsonify({"error": error}), 400
        if not item_data:
            return jsonify({"error": "Invalid payload."}), 400
        item_data["id"] = item_data["id"] or _next_item_id(items)
        items.insert(0, item_data)
        _save_items(items)
    return jsonify({"item": item_data, "items": items}), 201
@app.post("/api/items/<item_id>/restock")
def restock_item(item_id: str) -> Any:
    payload = request.get_json(silent=True) or {}
    units = int(_to_non_negative_number(payload.get("units")) or 10)
    if units <= 0:
        return jsonify({"error": "Units must be greater than zero."}), 400
    with _DATA_LOCK:
        items = _load_items()
        index = _find_item_index(items, item_id)
        if index < 0:
            return jsonify({"error": "Item not found."}), 404

        items[index]["quantity"] += units
        _save_items(items)

    return jsonify({"item": items[index], "items": items})
@app.post("/api/items/<item_id>/sell")
def sell_item(item_id: str) -> Any:
    payload = request.get_json(silent=True) or {}
    units = int(_to_non_negative_number(payload.get("units")) or 1)
    if units <= 0:
        return jsonify({"error": "Units must be greater than zero."}), 400
    with _DATA_LOCK:
        items = _load_items()
        index = _find_item_index(items, item_id)
        if index < 0:
            return jsonify({"error": "Item not found."}), 404

        if items[index]["quantity"] < units:
            return jsonify({"error": "Not enough stock for this sale."}), 400

        items[index]["quantity"] -= units
        _save_items(items)
    return jsonify({"item": items[index], "items": items})


@app.post("/api/items/<item_id>/sell-all")
def sell_all_for_item(item_id: str) -> Any:
    with _DATA_LOCK:
        items = _load_items()
        index = _find_item_index(items, item_id)
        if index < 0:
            return jsonify({"error": "Item not found."}), 404

        sold_units = items[index]["quantity"]
        items[index]["quantity"] = 0
        _save_items(items)

    return jsonify({"item": items[index], "sold_units": sold_units, "items": items})
@app.delete("/api/items/<item_id>")
def delete_item(item_id: str) -> Any:
    with _DATA_LOCK:
        items = _load_items()
        index = _find_item_index(items, item_id)
        if index < 0:
            return jsonify({"error": "Item not found."}), 404

        deleted = items.pop(index)
        _save_items(items)

    return jsonify({"deleted": deleted, "items": items})


@app.delete("/api/items")
def clear_items() -> Any:
    with _DATA_LOCK:
        items: list[dict[str, Any]] = []
        _save_items(items)
    return jsonify({"items": items})


@app.post("/api/items/restock-all")
def restock_all_items() -> Any:
    payload = request.get_json(silent=True) or {}
    units = int(_to_non_negative_number(payload.get("units")) or 10)
    if units <= 0:
        return jsonify({"error": "Units must be greater than zero."}), 400

    with _DATA_LOCK:
        items = _load_items()
        for item in items:
            item["quantity"] += units
        _save_items(items)

    return jsonify({"items": items, "units_added_per_item": units})


@app.post("/api/items/sell-all")
def sell_all_items() -> Any:
    with _DATA_LOCK:
        items = _load_items()
        total_sold_units = sum(int(item.get("quantity", 0)) for item in items)
        for item in items:
            item["quantity"] = 0
        _save_items(items)

    return jsonify({"items": items, "total_sold_units": total_sold_units})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
