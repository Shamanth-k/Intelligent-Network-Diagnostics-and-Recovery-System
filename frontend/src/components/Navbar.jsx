import React from "react";
import { Link, useLocation } from "react-router-dom";

export default function Navbar() {
  const location = useLocation();

  const navLink = (path, label) => (
    <Link
      to={path}
      className={`px-4 py-2 rounded-md transition ${
        location.pathname === path
          ? "bg-cyan-600 text-white"
          : "text-gray-300 hover:bg-slate-700"
      }`}
    >
      {label}
    </Link>
  );

  return (
    <nav className="flex justify-between items-center p-4 bg-slate-800 border-b border-slate-700">
      <h1 className="text-2xl font-bold text-cyan-400">IntelliNet</h1>
      <div className="flex gap-3">
        {navLink("/", "Dashboard")}
        {navLink("/settings", "Settings")}
      </div>
    </nav>
  );
}
