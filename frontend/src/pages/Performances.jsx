import { useEffect, useState } from "react";
import { getPerformances } from "../api";

function ytToEmbed(url) {
  try {
    const u = new URL(url);
    if (u.hostname.includes("youtube.com") && u.searchParams.get("v")) {
      return `https://www.youtube.com/embed/${u.searchParams.get("v")}`;
    }
    if (u.hostname.includes("youtu.be")) {
      return `https://www.youtube.com/embed/${u.pathname.slice(1)}`;
    }
    return url;
  } catch { return url; }
}

export default function Performances() {
  const [items, setItems] = useState([]);
  const [q, setQ] = useState("");
  const [artForm, setArtForm] = useState("");
  const [loading, setLoading] = useState(false);

  async function load() {
    setLoading(true);
    try {
      const data = await getPerformances({
        q: q || undefined,
        art_form: artForm || undefined,
      });
      setItems(data);
    } catch {
      setItems([]);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => { load(); }, []);

  return (
    <div className="space-y-6">
      <div className="text-center">
        <h1 className="text-3xl font-heading font-bold">Performances</h1>
        <p className="text-brand-brown/70">Search and explore recorded arts</p>
      </div>

      <div className="flex flex-col md:flex-row gap-3">
        <input
          value={q}
          onChange={(e) => setQ(e.target.value)}
          placeholder="Search title / artist / tags…"
          className="border border-brand-brown/20 bg-white rounded-card px-4 py-2 flex-1"
        />
        <input
          value={artForm}
          onChange={(e) => setArtForm(e.target.value)}
          placeholder="Art form (e.g., Bharatanatyam)"
          className="border border-brand-brown/20 bg-white rounded-card px-4 py-2"
        />
        <button
          onClick={load}
          className="px-5 py-2 rounded-card bg-brand-green text-white hover:brightness-110"
        >
          Search
        </button>
      </div>

      {loading && <p className="text-brand-brown/70">Loading…</p>}

      <div className="grid md:grid-cols-2 gap-6">
        {items.map((it) => (
          <div key={it.id} className="bg-brand-card border border-brand-brown/10 rounded-card shadow-soft overflow-hidden">
            <div className="aspect-video bg-black">
              <iframe
                className="w-full h-full"
                src={ytToEmbed(it.video_url)}
                title={it.title}
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              />
            </div>
            <div className="p-4">
              <div className="font-heading text-lg font-semibold">{it.title}</div>
              <div className="text-sm text-brand-brown/70">{it.artist} • {it.art_form} • {it.year || "—"}</div>
              {it.description && <div className="text-sm mt-2">{it.description}</div>}
              {it.tags && (
                <div className="mt-3 flex flex-wrap gap-2">
                  {it.tags.split(",").map((t) => (
                    <span key={t} className="text-xs bg-brand-bg px-2 py-1 rounded-full border border-brand-brown/10">
                      {t.trim()}
                    </span>
                  ))}
                </div>
              )}
            </div>
          </div>
        ))}
      </div>

      {!loading && items.length === 0 && (
        <p className="text-brand-brown/60">No results. Try another search.</p>
      )}
    </div>
  );
}
