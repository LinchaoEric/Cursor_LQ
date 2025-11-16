"use client";

import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useMemo,
  useReducer,
} from "react";
import type { Book, BookDraft, BookStatus } from "@/lib/types";

const STORAGE_KEY = "bookshelf-books";

type BookAction =
  | { type: "SET"; payload: Book[] }
  | { type: "ADD"; payload: Book }
  | { type: "UPDATE"; payload: { id: string; updates: Partial<Book> } }
  | { type: "REMOVE"; payload: { id: string } };

interface BookState {
  books: Book[];
}

interface BookContextValue {
  books: Book[];
  addBook: (draft: BookDraft) => void;
  updateStatus: (id: string, status: BookStatus) => void;
  updateBook: (id: string, updates: Partial<Book>) => void;
  removeBook: (id: string) => void;
}

const BookContext = createContext<BookContextValue | undefined>(undefined);

const initialState: BookState = {
  books: [],
};

function bookReducer(state: BookState, action: BookAction): BookState {
  switch (action.type) {
    case "SET":
      return { books: action.payload };
    case "ADD":
      return { books: [action.payload, ...state.books] };
    case "UPDATE":
      return {
        books: state.books.map((book) =>
          book.id === action.payload.id
            ? { ...book, ...action.payload.updates }
            : book
        ),
      };
    case "REMOVE":
      return {
        books: state.books.filter((book) => book.id !== action.payload.id),
      };
    default:
      return state;
  }
}

function generateId() {
  if (typeof crypto !== "undefined" && "randomUUID" in crypto) {
    return crypto.randomUUID();
  }
  return Math.random().toString(36).slice(2);
}

const sampleBooks: Book[] = [
  {
    id: "sample-1",
    title: "Atomic Habits",
    author: "James Clear",
    coverUrl: "https://images-na.ssl-images-amazon.com/images/I/91bYsX41DVL.jpg",
    status: "reading",
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  },
  {
    id: "sample-2",
    title: "Deep Work",
    author: "Cal Newport",
    coverUrl:
      "https://images-na.ssl-images-amazon.com/images/I/41aA4QFzy9L._SX331_BO1,204,203,200_.jpg",
    status: "to_read",
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  },
  {
    id: "sample-3",
    title: "The Psychology of Money",
    author: "Morgan Housel",
    coverUrl:
      "https://images-na.ssl-images-amazon.com/images/I/71g2ednj0JL.jpg",
    status: "finished",
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  },
];

export function BookProvider({ children }: { children: React.ReactNode }) {
  const [state, dispatch] = useReducer(bookReducer, initialState);

  useEffect(() => {
    const stored =
      typeof window !== "undefined"
        ? window.localStorage.getItem(STORAGE_KEY)
        : null;
    if (stored) {
      try {
        const parsed: Book[] = JSON.parse(stored);
        dispatch({ type: "SET", payload: parsed });
        return;
      } catch {
        // ignore corrupted storage and overwrite below
      }
    }
    dispatch({ type: "SET", payload: sampleBooks });
  }, []);

  useEffect(() => {
    if (typeof window === "undefined") return;
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(state.books));
  }, [state.books]);

  const addBook = useCallback((draft: BookDraft) => {
    const now = new Date().toISOString();
    const book: Book = {
      id: generateId(),
      title: draft.title.trim(),
      author: draft.author?.trim() || undefined,
      coverUrl: draft.coverUrl?.trim() || null,
      status: "to_read",
      createdAt: now,
      updatedAt: now,
    };
    dispatch({ type: "ADD", payload: book });
  }, []);

  const updateStatus = useCallback((id: string, status: BookStatus) => {
    dispatch({
      type: "UPDATE",
      payload: { id, updates: { status, updatedAt: new Date().toISOString() } },
    });
  }, []);

  const updateBook = useCallback((id: string, updates: Partial<Book>) => {
    dispatch({
      type: "UPDATE",
      payload: { id, updates: { ...updates, updatedAt: new Date().toISOString() } },
    });
  }, []);

  const removeBook = useCallback((id: string) => {
    dispatch({ type: "REMOVE", payload: { id } });
  }, []);

  const value = useMemo(
    () => ({
      books: state.books,
      addBook,
      updateStatus,
      updateBook,
      removeBook,
    }),
    [state.books, addBook, updateStatus, updateBook, removeBook]
  );

  return <BookContext.Provider value={value}>{children}</BookContext.Provider>;
}

export function useBooks() {
  const context = useContext(BookContext);
  if (!context) {
    throw new Error("useBooks must be used within a BookProvider");
  }
  return context;
}
