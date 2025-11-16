"use client";

import { useMemo, useState } from "react";
import AddBookForm from "@/components/AddBookForm";
import BookCard from "@/components/BookCard";
import BookDetailPanel from "@/components/BookDetailPanel";
import StatusTabs from "@/components/StatusTabs";
import { useBooks } from "@/context/BookContext";
import type { BookStatus } from "@/lib/types";
import { STATUS_META } from "@/lib/status";

export default function HomePage() {
  const { books } = useBooks();
  const [activeStatus, setActiveStatus] = useState<BookStatus>("reading");
  const [selectedBookId, setSelectedBookId] = useState<string | null>(null);

  const filteredBooks = useMemo(
    () => books.filter((book) => book.status === activeStatus),
    [books, activeStatus]
  );

  const visibleBookId = useMemo(() => {
    if (!filteredBooks.length) return null;
    if (
      selectedBookId &&
      filteredBooks.some((book) => book.id === selectedBookId)
    ) {
      return selectedBookId;
    }
    return filteredBooks[0].id;
  }, [filteredBooks, selectedBookId]);

  const selectedBook = useMemo(
    () => books.find((book) => book.id === visibleBookId) ?? null,
    [books, visibleBookId]
  );

  return (
    <div className="px-4 py-10 sm:px-8">
      <div className="mx-auto flex w-full max-w-6xl flex-col gap-10">
        <header className="flex flex-col gap-4">
          <p className="text-sm font-semibold uppercase tracking-[0.25em] text-slate-500">
            Personal bookshelf
          </p>
          <div className="flex flex-col gap-3 lg:flex-row lg:items-end lg:justify-between">
            <div>
              <h1 className="text-4xl font-semibold text-slate-900">
                Manage everything you&apos;re reading
              </h1>
              <p className="text-base text-slate-500">
                Three lightweight lists to keep track of books you want to read,
                are reading now, and have finished.
              </p>
            </div>
            <div className="text-sm text-slate-500">
              {books.length} total books
            </div>
          </div>
        </header>

        <StatusTabs active={activeStatus} onChange={setActiveStatus} />

        <section className="grid gap-8 lg:grid-cols-[2fr,1fr]">
          <div className="flex flex-col gap-6">
            <AddBookForm />
            <div className="rounded-3xl border border-slate-200 bg-white/80 p-6 shadow-sm">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <div>
                  <p className="text-sm font-medium uppercase tracking-wide text-slate-500">
                    Shelf
                  </p>
                  <h2 className="text-2xl font-semibold text-slate-900">
                    {STATUS_META[activeStatus].label}
                  </h2>
                </div>
                <span className="text-sm text-slate-500">
                  {filteredBooks.length} items
                </span>
              </div>

              {filteredBooks.length ? (
                <div className="mt-6 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
                  {filteredBooks.map((book) => (
                    <BookCard
                      key={book.id}
                      book={book}
                      isActive={visibleBookId === book.id}
                      onSelect={(item) => setSelectedBookId(item.id)}
                    />
                  ))}
                </div>
              ) : (
                <EmptyShelfMessage status={activeStatus} />
              )}
            </div>
          </div>
          <BookDetailPanel book={selectedBook} />
        </section>
      </div>
    </div>
  );
}

function EmptyShelfMessage({ status }: { status: BookStatus }) {
  return (
    <div className="mt-6 rounded-3xl border border-dashed border-slate-200 bg-white/70 p-6 text-sm text-slate-500">
      <p className="font-semibold text-slate-600">
        No books in {STATUS_META[status].label}.
      </p>
      <p>Add a book using the form above or switch to another tab.</p>
    </div>
  );
}
