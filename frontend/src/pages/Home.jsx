// src/pages/Home.jsx
import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div className="space-y-10">
      {/* Header */}
      <div className="text-center">
        <h1 className="text-4xl font-heading font-bold">Welcome to Kala</h1>
        <p className="text-brand-brown/70 mt-2">
          A platform to celebrate, preserve, and revive the arts
        </p>
      </div>

      {/* Feature cards */}
      <div className="grid md:grid-cols-3 gap-6 max-w-5xl mx-auto">
        <Link
          to="/performances"
          className="bg-brand-card border border-brand-brown/10 rounded-card shadow-soft p-6 hover:shadow-lg transition"
        >
          <h2 className="font-heading text-xl mb-2">Performances</h2>
          <p className="text-brand-brown/70 text-sm">
            Explore recorded performances from classical to contemporary arts.
          </p>
        </Link>

        <Link
          to="/ask"
          className="bg-brand-card border border-brand-brown/10 rounded-card shadow-soft p-6 hover:shadow-lg transition"
        >
          <h2 className="font-heading text-xl mb-2">Ask Kala</h2>
          <p className="text-brand-brown/70 text-sm">
            Ask about art forms and get concise, accessible answers.
          </p>
        </Link>

        <Link
          to="/revival"
          className="bg-brand-card border border-brand-brown/10 rounded-card shadow-soft p-6 hover:shadow-lg transition"
        >
          <h2 className="font-heading text-xl mb-2">Revival</h2>
          <p className="text-brand-brown/70 text-sm">
            Learn about endangered and rare art forms, and how they can be
            revived.
          </p>
        </Link>
      </div>

      {/* Hero image block */}
      <div className="max-w-5xl mx-auto mt-8">
        <img
          src="/kala.jpg"
          alt="Kala — celebration of arts"
          className="w-full rounded-card shadow-soft border border-brand-brown/10"
        />
      </div>
    </div>
  );
}
