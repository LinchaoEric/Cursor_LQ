"use client";

import { BookProvider } from "./BookContext";

export function Providers({ children }: { children: React.ReactNode }) {
  return <BookProvider>{children}</BookProvider>;
}
