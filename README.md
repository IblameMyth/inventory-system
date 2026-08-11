<div align="center">

  <img src="https://capsule-render.vercel.app/api?type=waving&color=6366F1&height=200&section=header&text=Inventory%20System&fontSize=60&animation=fadeIn" width="100%" alt="Header Banner" />

  <p align="center">
    <b>📦 Full-Stack Automated Inventory & Asset Management Platform</b><br />
    <i>Features severe-fallback offline resilience, serverless Vercel API routes, Firebase integration, and CI/CD deployment pipelines.</i>
  </p>

  <!-- Badges -->
  <p align="center">
    <a href="#">
      <img src="https://img.shields.io/badge/Architecture-FullStack-6366F1?style=for-the-badge" alt="Architecture" />
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/Deployment-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel" />
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" alt="GitHub Actions" />
    </a>
    <a href="#">
      <img src="https://img.shields.io/badge/Backend-Node.js_--%3E_Serverless-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js" />
    </a>
  </p>

  <p align="center">
    <a href="#-key-features"><b>⚡ Features</b></a> •
    <a href="#-tech-stack"><b>🛠️ Tech Stack</b></a> •
    <a href="#-project-architecture"><b>📂 Directory Layout</b></a> •
    <a href="#-quick-start"><b>🚀 Getting Started</b></a>
  </p>

  <br />

</div>

---

## ⚡ Key Architectural Features

- 🔄 **Full-Stack Decoupled Architecture:** Clean separation of client frontend (`/front_end`), serverless endpoints (`/api`), and core backend service business logic (`/backend`).
- 🛡️ **Hardened Offline Fallback:** Custom client-side resilience mechanisms ensuring per-item offline caching and fallback handling on hosted pages.
- ⚡ **Serverless Vercel Deployment:** Production API layer powered by Vercel serverless functions configured via `vercel.json`.
- 🔥 **Firebase Services Integration:** Pre-configured Firebase ecosystem setup with custom `.firebaserc` and `firebase.json` target configs.
- ⚙️ **Automated CI/CD Workflows:** Automated deployment and checks running via `.github/workflows` GitHub Actions pipeline.

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
| :--- | :--- |
| **Frontend UI** | <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" /> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" /> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" /> |
| **Serverless & Runtime** | <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" /> <img src="https://img.shields.io/badge/Vercel_Functions-000000?style=for-the-badge&logo=vercel&logoColor=white" /> |
| **Cloud & Storage** | <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black" /> |
| **DevOps & CI/CD** | <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white" /> |

</div>

---

## 📂 Project Architecture

Based on the repository source tree:

```bash
Inventory-System/
├── 📁 .github/workflows/   # GitHub Actions automated deployment scripts
├── 📁 .vscode/             # Editor workspace configs
├── 📁 api/                 # Vercel serverless API endpoint functions
├── 📁 backend/             # Core backend business logic & routines
├── 📁 front_end/           # Client-side UI & offline resilience scripts
├── 📁 node_modules/        # Project packages & dependencies
├── 📄 .firebaserc          # Firebase project alias configurations
├── 📄 .gitattributes       # Git path attributes
├── 📄 firebase.json        # Firebase hosting/services config
├── 📄 package.json         # Node.js project manifest & scripts
├── 📄 package-lock.json    # Exact dependency tree lockfile
├── 📄 vercel.json          # Vercel deployment routes & configuration
└── 📄 README.md            # Repository documentation
## Notes

- If Firestore credentials are not configured, the backend falls back to JSON storage.
- Generated files like `node_modules`, logs, and cache files should not be committed.
