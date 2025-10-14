import React, { useEffect, useState } from "react";
import NetworkStatusCard from "../components/NetworkStatusCard";
import NetworkFixPanel from "../components/NetworkFixPanel";
import LogsTable from "../components/LogsTable";
import { fetchMetrics, fetchLogs } from "../utils/api";

export default function Dashboard() {
  const [metrics, setMetrics] = useState({});
  const [logs, setLogs] = useState([]);

  const loadData = async () => {
    const m = await fetchMetrics();
    setMetrics(m);
    const l = await fetchLogs(50);
    setLogs(l.logs || []);
  };

  useEffect(() => {
    loadData();
    const interval = setInterval(loadData, 7000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex flex-col items-center gap-6">
      <NetworkStatusCard metrics={metrics} />
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full max-w-5xl">
        <NetworkFixPanel />
        <LogsTable logs={logs} />
      </div>
    </div>
  );
}
useEffect(() => {
  const ws = new WebSocket("ws://127.0.0.1:8000/ws/logs");

  ws.onopen = () => console.log("WebSocket connected");
  ws.onmessage = (event) => {
    const log = JSON.parse(event.data);
    setLogs((prev) => [...prev.slice(-49), log]); // keep last 50
  };
  ws.onclose = () => console.log("WebSocket disconnected");

  return () => ws.close();
}, []);
