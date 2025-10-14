Here’s a professional **README.md** for your IntelliNet project, covering setup, features, and usage:

```markdown
# IntelliNet

IntelliNet is a real-time network monitoring and auto-fix tool built with **React.js** (frontend) and **FastAPI** (backend). It continuously monitors network hosts, logs status, and provides automated fixes like DNS flush and network adapter restart.

---

## 🖥 Project Structure

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
├── monitoring_daemon/      # Python monitoring daemon
│   ├── monitor.py
│   └── config.json
├── database/               # Optional DB setup
│   └── setup.js
├── docker-compose.yml      # Optional
└── README.md

````

---

## ⚡ Features

- **Real-time network monitoring** using ping for multiple hosts.
- **Automated fixes**:
  - Flush DNS
  - Restart network adapter
- **Network metrics**: Health status counts (Healthy, Warning, Critical, Info)
- **Logs table**: Last 50 network events displayed dynamically.
- **Frontend**: React.js + TailwindCSS.
- **Backend**: FastAPI with WebSocket support for live updates.

---

## 🚀 Installation

### Backend

1. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
````

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Start the backend server:

```bash
uvicorn main:app --reload
```

The backend will run at `http://127.0.0.1:8000`.

---

### Frontend

1. Navigate to frontend folder:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
```

3. Start the frontend server:

```bash
npm run dev
```

The frontend will run at `http://localhost:5173`.

---

### Monitoring Daemon

1. Ensure the backend is running.
2. Start the daemon to begin real-time monitoring:

```bash
python monitoring_daemon/monitor.py
```

---

## 🛠 Usage

* Open the frontend in your browser.
* Dashboard shows:

  * **Metrics Card**: Overall network status counts.
  * **Logs Table**: Recent network events.
  * **Auto-fix Panel**: Trigger fixes like DNS flush or adapter restart.
* Logs update **instantly** in real-time via WebSockets.

---

## ⚙ Configuration

* **Hosts to monitor**: Edit `monitoring_daemon/monitor.py` → `hosts_to_monitor` list.
* **Backend URL**: Frontend will dynamically use `localStorage.getItem("BASE_URL")` or default `http://127.0.0.1:8000`.

---

## 📝 Notes

* Currently using **in-memory logs**. For production, connect to **MongoDB or PostgreSQL**.
* Keep WebSocket port open for real-time updates.
* TailwindCSS is used for styling; modify `tailwind.config.js` for theme changes.

---

## 💡 Future Improvements

* Add **user authentication**.
* Persist logs in a database.
* Dynamic alerting system (emails, SMS).
* Dashboard metrics graph visualization.

---

## License

MIT License © 2025 IntelliNet

```

---

I can also create a **shorter “developer quick-start” README** optimized for contributors if you want.  

Do you want me to do that too?
```
