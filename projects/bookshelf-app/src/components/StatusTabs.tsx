"use client";

import { STATUS_LIST, STATUS_META } from "@/lib/status";
import type { BookStatus } from "@/lib/types";

interface Props {
  active: BookStatus;
  onChange: (status: BookStatus) => void;
}

export default function StatusTabs({ active, onChange }: Props) {
  return (
    <div className="flex flex-wrap gap-2 rounded-3xl border border-slate-200 bg-white/80 p-1.5 shadow-sm">
      {STATUS_LIST.map((status) => (
        <button
          key={status}
          type="button"
          onClick={() => onChange(status)}
          className={`flex flex-1 min-w-[120px] flex-col rounded-2xl px-4 py-2 text-left transition ${
            active === status
              ? "bg-slate-900 text-white"
              : "text-slate-600 hover:bg-slate-100"
          }`}
        >
          <span className="text-sm font-semibold">
            {STATUS_META[status].label}
          </span>
          {active === status && (
            <span className="text-xs text-white/70">
              {STATUS_META[status].description}
            </span>
          )}
        </button>
      ))}
    </div>
  );
}
