// src/utils/api.js

// Dynamically get backend URL from localStorage or fallback to default
const BASE_URL = localStorage.getItem("BASE_URL") || "http://127.0.0.1:8000";

/**
 * Fetch overall network metrics (Healthy, Warning, Critical counts)
 */
export async function fetchMetrics() {
  try {
    const res = await fetch(`${BASE_URL}/api/metrics/status`);
    if (!res.ok) throw new Error("Failed to fetch network metrics");
    return await res.json();
  } catch (err) {
    console.error("fetchMetrics error:", err);
    return {};
  }
}

/**
 * Fetch recent network logs
 * @param {number} limit Number of logs to fetch
 */
export async function fetchLogs(limit = 50) {
  try {
    const res = await fetch(`${BASE_URL}/api/logs?limit=${limit}`);
    if (!res.ok) throw new Error("Failed to fetch logs");
    return await res.json();
  } catch (err) {
    console.error("fetchLogs error:", err);
    return { logs: [] };
  }
}

/**
 * Trigger auto-fix actions on the backend
 * @param {string} action Action name, e.g., "flush-dns", "restart-adapter"
 */
export async function callFix(action) {
  try {
    const res = await fetch(`${BASE_URL}/api/fix/${action}`, {
      method: "POST",
    });

    if (!res.ok) {
      const text = await res.text();
      throw new Error(text || "Auto-fix failed");
    }

    return await res.json();
  } catch (err) {
    console.error("callFix error:", err);
    throw err;
  }
}
