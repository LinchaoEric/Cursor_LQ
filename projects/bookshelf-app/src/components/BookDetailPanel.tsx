"use client";

import { STATUS_LIST, STATUS_META } from "@/lib/status";
import type { Book } from "@/lib/types";
import { useBooks } from "@/context/BookContext";

interface Props {
  book?: Book | null;
}

export default function BookDetailPanel({ book }: Props) {
  const { updateStatus, removeBook } = useBooks();

  if (!book) {
    return (
      <div className="flex h-full items-center justify-center rounded-3xl border border-dashed border-slate-200 bg-white/60 px-6 text-center text-sm text-slate-500">
        Select a book from your shelf to see its details.
      </div>
    );
  }

  const handleStatusChange = (status: Book["status"]) => {
    updateStatus(book.id, status);
  };

  const handleRemove = () => {
    const confirmRemove =
      typeof window !== "undefined"
        ? window.confirm(`Remove "${book.title}" from your shelf?`)
        : true;
    if (confirmRemove) {
      removeBook(book.id);
    }
  };

  return (
    <section className="flex h-full flex-col gap-6 rounded-3xl border border-slate-200 bg-white/80 p-6 shadow-sm">
      <div className="flex flex-col gap-2">
        <p className="text-sm font-medium uppercase tracking-wide text-slate-500">
          Book Details
        </p>
        <h3 className="text-2xl font-semibold text-slate-900">{book.title}</h3>
        {book.author && (
          <p className="text-base text-slate-500">by {book.author}</p>
        )}
      </div>
      <div className="grid gap-4">
        <div className="grid gap-2">
          <span className="text-xs font-semibold uppercase tracking-widest text-slate-500">
            Current status
          </span>
          <div className="flex flex-wrap gap-2">
            {STATUS_LIST.map((status) => (
              <button
                key={status}
                type="button"
                onClick={() => handleStatusChange(status)}
                className={`rounded-full px-4 py-1.5 text-sm font-medium transition ${
                  book.status === status
                    ? "bg-slate-900 text-white shadow"
                    : "bg-slate-100 text-slate-600 hover:bg-slate-200"
                }`}
              >
                {STATUS_META[status].label}
              </button>
            ))}
          </div>
        </div>
        <div className="grid gap-2">
          <span className="text-xs font-semibold uppercase tracking-widest text-slate-500">
            Notes
          </span>
          <p className="rounded-2xl border border-dashed border-slate-200 bg-white p-4 text-sm text-slate-500">
            Future space for reading progress, highlights, and reflections.
          </p>
        </div>
      </div>
      <div className="mt-auto flex justify-end">
        <button
          type="button"
          onClick={handleRemove}
          className="text-sm font-medium text-rose-500 underline-offset-4 hover:underline"
        >
          Remove from shelf
        </button>
      </div>
    </section>
  );
}
