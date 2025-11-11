
# ⚙️ IntelliNet

**IntelliNet** is a real-time **network monitoring and auto-healing system** built with **React.js** (frontend) and **FastAPI** (backend).  
It continuously tracks network hosts, logs their health status, and automatically triggers fixes like DNS flushing and network adapter restarts.

---

## 📁 Project Structure

```

IntelliNet/
├── backend/                # FastAPI backend
│   ├── main.py
│   ├── auto_fix.py
│   ├── routes/
│   │   ├── logs.py
│   │   ├── metrics.py
│   │   └── ws.py
│   └── models/
│       └── log_model.py
├── frontend/               # React.js frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── NetworkStatusCard.jsx
│   │   │   ├── NetworkFixPanel.jsx
│   │   │   └── LogsTable.jsx
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   └── Settings.jsx
│   │   ├── utils/
│   │   │   └── api.js
│   │   └── index.jsx
│   └── index.html
├── monitoring_daemon/      # Python daemon for continuous monitoring
│   ├── monitor.py
│   └── config.json
├── database/               # (Optional) Database setup
│   └── setup.js
├── docker-compose.yml      # (Optional) Containerized setup
└── README.md

````


## 🚨 Key Features

- **Real-time monitoring** of multiple hosts using ICMP ping.  
- **Automatic network recovery actions**, including:
  - DNS cache flush  
  - Network adapter restart  
- **Dynamic dashboard** with:
  - Health metrics (Healthy / Warning / Critical)  
  - Real-time event logs via WebSockets  
  - Manual “Auto-Fix” triggers  
- **Modern stack**:
  - **Frontend**: React.js + Tailwind CSS  
  - **Backend**: FastAPI + WebSocket  

---

## ⚙️ Installation Guide

### 🧩 Backend Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
# Activate
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Backend runs on: `http://127.0.0.1:8000`

---

### 💻 Frontend Setup

1. Navigate to the frontend directory:

```bash
cd frontend
```

2. Install dependencies and start the app:

```bash
npm install
npm run dev
```

Frontend runs on: `http://localhost:5173`

---

### 🛰 Monitoring Daemon

1. Ensure the backend is running.
2. Start real-time monitoring:

```bash
python monitoring_daemon/monitor.py
```

The daemon will continuously ping configured hosts and stream updates via WebSocket.

---

## 🧭 Usage

1. Open the dashboard in your browser.
2. View:

   * **Metrics Panel**: Displays live host health counts.
   * **Logs Table**: Lists latest 50 network events.
   * **Fix Panel**: Allows triggering network repair actions.
3. Data updates automatically in **real-time** — no refresh required.

---

## ⚙️ Configuration

* **Monitored hosts**: Edit `hosts_to_monitor` inside `monitoring_daemon/monitor.py`.
* **Backend API URL**: Controlled via `localStorage.getItem("BASE_URL")` or defaults to `http://127.0.0.1:8000`.

---

## 🗒 Notes

* Currently, logs are **stored in memory**. For persistence, integrate **MongoDB** or **PostgreSQL**.
* Ensure the WebSocket port is open for live updates.
* TailwindCSS can be customized in `tailwind.config.js`.

---


