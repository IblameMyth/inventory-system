# Inventory System

A small inventory management app with a Flask backend and a static web front end.

## What it does

- Add inventory items
- Restock or sell stock
- Track low-stock items
- Save data locally in JSON or use Firestore when configured

## Project Layout

- `backend/` - Flask API and inventory logic
- `front_end/` - Static UI
- `api/` - Vercel serverless entry point
- `vercel.json` - Vercel routing config

## Local Run

### Backend

```bash
cd backend
python inventory_system.py
```

The app runs on `http://127.0.0.1:8080` by default.

### Front end

Open `front_end/index.html` in a browser, or serve the folder with a local static server.

## Vercel Deploy

This repository is set up for Vercel through `vercel.json` and `api/index.py`.

Deploy steps:

1. Push the repo to GitHub.
2. Import the repository into Vercel.
3. Let Vercel detect the Python serverless function in `api/index.py`.
4. Deploy the project.

## Notes

- If Firestore credentials are not configured, the backend falls back to JSON storage.
- Generated files like `node_modules`, logs, and cache files should not be committed.