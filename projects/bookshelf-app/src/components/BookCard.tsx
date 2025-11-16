"use client";

import type { Book } from "@/lib/types";
import { STATUS_META } from "@/lib/status";

interface Props {
  book: Book;
  isActive: boolean;
  onSelect: (book: Book) => void;
}

export default function BookCard({ book, isActive, onSelect }: Props) {
  const coverImage = book.coverUrl || "";

  return (
    <button
      type="button"
      onClick={() => onSelect(book)}
      className={`group flex h-full flex-col rounded-3xl border bg-white/80 text-left shadow-sm transition hover:-translate-y-1 hover:shadow-lg ${
        isActive ? "border-slate-900/70" : "border-slate-100"
      }`}
    >
      <div className="relative aspect-[3/4] overflow-hidden rounded-3xl bg-gradient-to-br from-slate-100 to-slate-200">
        {coverImage ? (
          // eslint-disable-next-line @next/next/no-img-element
          <img
            src={coverImage}
            alt={book.title}
            className="h-full w-full object-cover"
          />
        ) : (
          <div className="flex h-full w-full flex-col items-center justify-center gap-1 text-center text-sm text-slate-500">
            <span className="font-semibold">No cover</span>
            <span>Add in details</span>
          </div>
        )}
      </div>
      <div className="flex flex-1 flex-col gap-2 p-4">
        <div className="text-sm font-medium text-slate-500">
          {STATUS_META[book.status].label}
        </div>
        <p className="text-base font-semibold text-slate-900 line-clamp-2">
          {book.title}
        </p>
        {book.author && (
          <p className="text-sm text-slate-500">{book.author}</p>
        )}
        <span className="text-xs uppercase tracking-widest text-slate-300">
          View details →
        </span>
      </div>
    </button>
  );
}
