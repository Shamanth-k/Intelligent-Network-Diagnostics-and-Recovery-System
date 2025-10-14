import React from "react";

export default function NetworkStatusCard({ metrics }) {
  const { total = 0, healthy = 0, warning = 0, critical = 0 } = metrics;
  const healthyPct = total ? Math.round((healthy / total) * 100) : 100;

  return (
    <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 w-full max-w-2xl">
      <h2 className="text-2xl font-bold text-cyan-300 mb-3">Network Summary</h2>
      <div className="grid grid-cols-3 gap-4">
        <div className="p-4 bg-slate-900 rounded-lg text-center">
          <p className="text-sm text-slate-300">Healthy</p>
          <p className="text-2xl text-green-300 font-semibold">{healthy}</p>
        </div>
        <div className="p-4 bg-slate-900 rounded-lg text-center">
          <p className="text-sm text-slate-300">Warning</p>
          <p className="text-2xl text-yellow-300 font-semibold">{warning}</p>
        </div>
        <div className="p-4 bg-slate-900 rounded-lg text-center">
          <p className="text-sm text-slate-300">Critical</p>
          <p className="text-2xl text-red-300 font-semibold">{critical}</p>
        </div>
      </div>

      <div className="mt-4">
        <p className="text-sm text-slate-400 mb-1">Healthy Rate</p>
        <div className="w-full h-3 bg-slate-700 rounded-full">
          <div
            className="h-3 bg-green-500 rounded-full"
            style={{ width: `${healthyPct}%` }}
          ></div>
        </div>
      </div>
    </div>
  );
}
