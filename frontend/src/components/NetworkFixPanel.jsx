import React, { useState } from "react";
import { callFix } from "../utils/api";

export default function NetworkFixPanel() {
  const [loading, setLoading] = useState(false);
  const [msg, setMsg] = useState(null);

  const handleFix = async (action) => {
    setLoading(true);
    setMsg(null);
    try {
      const res = await callFix(action);
      setMsg({ type: "success", text: res.message });
    } catch (err) {
      setMsg({ type: "error", text: err.message });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-md bg-slate-800 p-6 rounded-xl shadow-lg border border-slate-700">
      <h3 className="text-xl font-semibold text-cyan-300 mb-4">Network Auto-Fix</h3>

      <div className="flex gap-3 mb-3">
        <button
          onClick={() => handleFix("flush-dns")}
          disabled={loading}
          className="flex-1 py-2 bg-cyan-600 rounded-lg hover:bg-cyan-700 disabled:opacity-60"
        >
          {loading ? "Running..." : "Flush DNS"}
        </button>
        <button
          onClick={() => handleFix("restart-adapter")}
          disabled={loading}
          className="flex-1 py-2 bg-indigo-600 rounded-lg hover:bg-indigo-700 disabled:opacity-60"
        >
          {loading ? "Running..." : "Restart Adapter"}
        </button>
      </div>

      {msg && (
        <div
          className={`p-3 rounded-md ${
            msg.type === "success" ? "bg-green-700" : "bg-red-700"
          }`}
        >
          {msg.text}
        </div>
      )}
    </div>
  );
}
