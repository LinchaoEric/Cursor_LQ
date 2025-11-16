"use client";

import { useState } from "react";
import { useBooks } from "@/context/BookContext";

const emptyForm = {
  title: "",
  author: "",
  coverUrl: "",
};

export default function AddBookForm() {
  const { addBook } = useBooks();
  const [form, setForm] = useState(emptyForm);
  const [error, setError] = useState<string | null>(null);

  const handleChange = (
    event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    const { name, value } = event.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!form.title.trim()) {
      setError("Please add a book title.");
      return;
    }
    addBook({
      title: form.title,
      author: form.author || undefined,
      coverUrl: form.coverUrl || undefined,
    });
    setForm(emptyForm);
    setError(null);
  };

  return (
    <section className="rounded-3xl border border-slate-200 bg-white/80 p-6 shadow-sm backdrop-blur">
      <div className="flex flex-col gap-1">
        <p className="text-sm font-medium uppercase tracking-wide text-slate-500">
          Add Book
        </p>
        <h2 className="text-2xl font-semibold text-slate-900">
          Quick capture form
        </h2>
        <p className="text-sm text-slate-500">
          Title is required. You can add author and a cover URL later in the
          details view.
        </p>
      </div>
      <form className="mt-6 grid gap-4" onSubmit={handleSubmit}>
        <div className="grid gap-2">
          <label className="text-sm font-medium text-slate-600" htmlFor="title">
            Title *
          </label>
          <input
            id="title"
            name="title"
            value={form.title}
            onChange={handleChange}
            placeholder="E.g. The Almanack of Naval Ravikant"
            className="rounded-2xl border border-slate-200 px-3 py-2 text-base outline-none ring-slate-300 transition focus:ring-2"
          />
        </div>
        <div className="grid gap-2 md:grid-cols-2 md:gap-6">
          <div className="grid gap-2">
            <label
              className="text-sm font-medium text-slate-600"
              htmlFor="author"
            >
              Author
            </label>
            <input
              id="author"
              name="author"
              value={form.author}
              onChange={handleChange}
              placeholder="Optional"
              className="rounded-2xl border border-slate-200 px-3 py-2 text-base outline-none ring-slate-300 transition focus:ring-2"
            />
          </div>
          <div className="grid gap-2">
            <label
              className="text-sm font-medium text-slate-600"
              htmlFor="coverUrl"
            >
              Cover (URL)
            </label>
            <input
              id="coverUrl"
              name="coverUrl"
              value={form.coverUrl}
              onChange={handleChange}
              placeholder="Paste an image link (optional)"
              className="rounded-2xl border border-slate-200 px-3 py-2 text-base outline-none ring-slate-300 transition focus:ring-2"
            />
          </div>
        </div>
        {error && <p className="text-sm text-rose-500">{error}</p>}
        <div className="flex justify-end">
          <button
            type="submit"
            className="inline-flex items-center justify-center rounded-2xl bg-slate-900 px-4 py-2 text-sm font-semibold text-white shadow hover:bg-slate-800"
          >
            Save to bookshelf
          </button>
        </div>
      </form>
    </section>
  );
}
