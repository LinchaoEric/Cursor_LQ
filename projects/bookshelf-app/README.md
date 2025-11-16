# 📚 Bookshelf App (MVP)

A lightweight personal reading manager that keeps your books organized across the three core states from the PRD: **To Read**, **Reading**, and **Finished**. The entire experience runs locally in the browser using `localStorage`, so you can capture titles instantly without needing an account.

## ✨ Features

- **Quick add form** for title, author, and optional cover URL (default status is _To Read_).
- **Visual shelf tabs** that switch between To Read / Reading / Finished, defaulting to the Reading view per the PRD.
- **Card-based bookshelf grid** with placeholder art when no cover is provided.
- **Detail panel** showing book metadata, future notes space, and status-switch buttons.
- **Local persistence** powered by `localStorage`, so everything survives refreshes without a backend.

## 🧱 Tech Stack

- [Next.js 16 (App Router)](https://nextjs.org/)
- [React 19](https://react.dev/)
- [Tailwind CSS v4](https://tailwindcss.com/)
- TypeScript throughout the app

## 🚀 Getting Started

```bash
cd projects/bookshelf-app
npm install
npm run dev
```

Then open [http://localhost:3000](http://localhost:3000) to use the app.

## 🧪 Available Scripts

- `npm run dev` – start the local dev server with hot reload.
- `npm run lint` – run ESLint (Next.js config) to keep code quality high.
- `npm run build` / `npm start` – production build and preview.

## 🔮 Next Steps

The UI intentionally leaves room for the future roadmap outlined in the PRD: API-based book search, reading progress, highlights, yearly goals, and sync features can be layered onto the existing data structures and provider.
