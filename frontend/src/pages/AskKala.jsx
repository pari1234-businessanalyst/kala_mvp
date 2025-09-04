// src/pages/AskKala.jsx
import { useState } from "react";
import { askKala } from "../api";

const EXAMPLES = [
  "What is Bharatanatyam?",
  "Where does Odissi originate?",
  "Explain Kathak in brief.",
];

export default function AskKala() {
  const [q, setQ] = useState("");
  const [answer, setAnswer] = useState("");
  const [passages, setPassages] = useState([]);
  const [loading, setLoading] = useState(false);

  async function submit(text) {
    const query = (text ?? q).trim();
    if (!query) return;
    setLoading(true);
    setAnswer(""); setPassages([]);
    try {
      const res = await askKala(query);
      setAnswer(res.answer || "");
      setPassages(res.passages || []);
    } catch {
      setAnswer("Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-6 text-center">
      <h1 className="text-3xl font-heading font-bold">Ask Kala</h1>
      <p className="text-brand-brown/70">Ask about art forms and get concise answers</p>

      <div className="flex flex-col md:flex-row items-stretch gap-3 max-w-3xl mx-auto">
        <input
          value={q}
          onChange={(e) => setQ(e.target.value)}
          placeholder="e.g., What is Bharatanatyam?"
          className="border border-brand-brown/20 bg-white rounded-card px-4 py-3 flex-1"
          onKeyDown={(e) => e.key === "Enter" && submit()}
        />
        <button
          onClick={() => submit()}
          className="px-6 py-3 rounded-card bg-brand-green text-white hover:brightness-110"
        >
          Ask
        </button>
      </div>

      <div className="flex justify-center gap-2 flex-wrap">
        {EXAMPLES.map((ex) => (
          <button
            key={ex}
            onClick={() => submit(ex)}
            className="text-sm px-3 py-1 rounded-full border border-brand-brown/20 bg-white hover:bg-brand-bg"
          >
            {ex}
          </button>
        ))}
      </div>

      {loading && <p className="text-brand-brown/70">Thinking…</p>}

      {answer && (
        <div className="bg-brand-card border border-brand-brown/10 rounded-card shadow-soft p-5 max-w-3xl mx-auto text-left">
          <div className="font-heading font-semibold mb-2">Answer</div>
          <p>{answer}</p>
        </div>
      )}

      {passages?.length > 0 && (
        <div className="max-w-3xl mx-auto text-left">
          <div className="font-heading font-semibold mb-2">Sources</div>
          <ul className="space-y-2">
            {passages.map((p, i) => (
              <li key={i} className="bg-white border border-brand-brown/10 rounded-card p-3">
                <div className="text-xs text-brand-brown/60">{p.doc_path} • score {p.score?.toFixed(3)}</div>
                <div className="text-sm mt-1">{p.text}</div>
              </li>
            ))}
          </ul>
        </div>
      )}

      {!loading && !answer && (
        <p className="text-brand-brown/60">Try an example above, or ask your own question.</p>
      )}
    </div>
  );
}
