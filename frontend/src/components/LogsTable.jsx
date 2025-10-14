import React from "react";

export default function LogsTable({ logs = [] }) {
  return (
    <div className="bg-slate-800 p-4 rounded-xl border border-slate-700 overflow-x-auto">
      <h3 className="text-lg font-semibold text-cyan-300 mb-3">Recent Logs</h3>
      <table className="min-w-full text-left">
        <thead>
          <tr className="text-sm text-slate-400">
            <th className="py-2">Time</th>
            <th className="py-2">Target</th>
            <th className="py-2">Latency</th>
            <th className="py-2">Status</th>
            <th className="py-2">Details</th>
          </tr>
        </thead>
        <tbody>
          {logs.length === 0 ? (
            <tr>
              <td colSpan="5" className="text-center text-slate-400 py-4">
                No logs found
              </td>
            </tr>
          ) : (
            logs.map((log, i) => (
              <tr key={i} className="border-t border-slate-700">
                <td className="py-2 text-sm">{new Date(log.timestamp).toLocaleString()}</td>
                <td className="py-2 text-sm">{log.target}</td>
                <td className="py-2 text-sm">{log.latency ? `${(log.latency * 1000).toFixed(0)} ms` : "-"}</td>
                <td
                  className={`py-2 text-sm font-medium ${
                    log.status === "HEALTHY"
                      ? "text-green-300"
                      : log.status === "HIGH_LATENCY"
                      ? "text-yellow-300"
                      : "text-red-300"
                  }`}
                >
                  {log.status}
                </td>
                <td className="py-2 text-sm text-slate-300">{log.details || "-"}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}
