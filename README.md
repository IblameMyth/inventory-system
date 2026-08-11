<div align="center">

  <img src="https://capsule-render.vercel.app/api?type=waving&color=8B0000&height=200&section=header&text=INVENTORY%20CONTROL%20CENTER&fontSize=50&animation=fadeIn" width="100%" alt="Header Banner" />

  <p align="center">
    <b>🎓 COLLEGE MINI PROJECT | REAL-TIME INVENTORY MANAGEMENT DASHBOARD</b><br />
    <i>A sleek, modern interactive dashboard built for seamless stock tracking, real-time analytics, and quick catalog controls.</i>
  </p>

  <!-- Badges -->
  <p align="center">
    <a href="#">
      <img src="https://img.shields.io/badge/Project-College_Mini_Project-8B0000?style=for-the-badge&logo=academic&logoColor=white" alt="College Mini Project" />
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/UI-Dark_Gold_%26_Crimson-FFD700?style=for-the-badge&labelColor=1A0D0D" alt="UI Theme" />
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/Analytics-Real--Time-00F5FF?style=for-the-badge" alt="Real Time Analytics" />
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/Export-JSON_Data-10B981?style=for-the-badge&logo=json&logoColor=white" alt="JSON Export" />
    </a>
  </p>

  <p align="center">
    <a href="#-key-features"><b>⚡ Features</b></a> •
    <a href="#-dashboard-overview"><b>📊 Dashboard</b></a> •
    <a href="#-tech-stack"><b>🛠️ Tech Stack</b></a> •
    <a href="#-project-structure"><b>📂 Structure</b></a> •
    <a href="#-getting-started"><b>🚀 Quick Start</b></a>
  </p>

  <br />

</div>

---

## ⚡ Key Features

- 📊 **Live Inventory Analytics:** Monitor Total Products, Total Units, Total Inventory Value (Rs.), and Low Stock Alerts in real time.
- ⚡ **Batch Action Controls:** Instantly manage stock levels using built-in **"Restock All"** and **"Sell All Stock"** operations.
- 💾 **Data Export:** Built-in **"Download JSON"** functionality to backup and export your custom inventory catalog anytime.
- 🎨 **Premium Glassmorphism UI:** Crimson and Stark Gold dark-mode aesthetic with interactive stat cards and a responsive layout.
- 🕒 **Real-Time Clock & Timestamp:** Integrated header clock tracking exact operational timestamps.

---

## 📊 Dashboard Modules & Controls

<table>
  <tr>
    <td width="50%" align="center">
      <h3>🚀 Quick Action Hub</h3>
      <p>• <b>Download JSON:</b> Backup raw stock data.<br />• <b>Restock All:</b> Bulk update inventory levels.<br />• <b>Sell All Stock:</b> Instant stock reset option.</p>
    </td>
    <td width="50%" align="center">
      <h3>📈 Live Stat Metrics</h3>
      <p>• <b>Total Products:</b> Count of unique items.<br />• <b>Total Units:</b> Total available stock quantity.<br />• <b>Inventory Value:</b> Real-time valuation in Rs.<br />• <b>Low Stock:</b> Items needing restocking.</p>
    </td>
  </tr>
</table>

---

## 🛠️ Tech Stack & Architecture

<div align="center">

| Component | Technology / Tools |
| :--- | :--- |
| **Frontend UI** | <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" /> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" /> |
| **Theme & FX** | `Dark Gold & Crimson Palette` `Glassmorphism` `Flexbox/Grid Layout` `Responsive Cards` |
| **Data Format** | `JSON Data Serialization` `Local State Management` |

</div>

---

## 📂 Project Architecture

```bash
Inventory-System/
├── 📁 .github/workflows/   # Deployment pipelines
├── 📁 .vscode/             # Workspace settings
├── 📁 api/                 # Serverless endpoints
├── 📁 backend/             # Core backend logic
├── 📁 front_end/           # Dashboard UI source
├── 📄 index.html           # Main Control Center UI
├── 📄 package.json         # Dependencies & project scripts
└── 📄 README.md            # Project documentation

- If Firestore credentials are not configured, the backend falls back to JSON storage.
- Generated files like `node_modules`, logs, and cache files should not be committed.
