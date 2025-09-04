// src/pages/Revival.jsx
import { useEffect, useMemo, useState } from "react";
import { getRevival } from "../api";

function norm(s = "") {
  return s.toLowerCase().trim();
}

export default function Revival() {
  const [raw, setRaw] = useState([]);
  const [loading, setLoading] = useState(false);

  const [region, setRegion] = useState("");
  const [status, setStatus] = useState("");

  async function load() {
    setLoading(true);
    try {
      const data = await getRevival(); // no params; filter client-side
      setRaw(data || []);
    } catch {
      setRaw([]);
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => { load(); }, []);

  const filtered = useMemo(() => {
    let items = raw;
    if (region.trim()) {
      const r = norm(region);
      items = items.filter(it => norm(it.region || "").includes(r));
    }
    if (status.trim()) {
      const s = norm(status);
      items = items.filter(it => norm(it.status || "").includes(s));
    }
    return items;
  }, [raw, region, status]);

  return (
    <div className="space-y-6">
      <div className="text-center">
        <h1 className="text-3xl font-heading font-bold">Revival</h1>
        <p className="text-brand-brown/70">Endangered and legacy art forms</p>
      </div>

      <div className="flex flex-col md:flex-row gap-3">
        <input
          value={region}
          onChange={(e) => setRegion(e.target.value)}
          placeholder="Region (e.g., Bengal matches West Bengal)"
          className="border border-brand-brown/20 bg-white rounded-card px-4 py-2"
        />
        <input
          value={status}
          onChange={(e) => setStatus(e.target.value)}
          placeholder="Status (e.g., endangered)"
          className="border border-brand-brown/20 bg-white rounded-card px-4 py-2"
        />
        <button
          onClick={() => { setRegion(""); setStatus(""); }}
          className="px-4 py-2 rounded-card border border-brand-brown/20 bg-white hover:bg-brand-bg"
        >
          Clear
        </button>
      </div>

      <div className="text-sm text-brand-brown/60">
        {loading ? "Loading…" : `${filtered.length} result${filtered.length === 1 ? "" : "s"}`}
      </div>

      {loading && <p className="text-brand-brown/70">Loading…</p>}

      <div className="grid md:grid-cols-2 gap-6">
        {filtered.map((it) => (
          <div key={it.id} className="bg-brand-card border border-brand-brown/10 rounded-card shadow-soft p-5">
            <div className="font-heading text-lg font-semibold">{it.name}</div>
            <div className="text-sm text-brand-brown/70">{it.region || "—"} • {it.status || "—"}</div>
            {it.description && <div className="mt-2 text-sm">{it.description}</div>}
            {it.references && (
              <a className="text-brand-green text-sm mt-2 inline-block" href={it.references} target="_blank" rel="noreferrer">
                Reference
              </a>
            )}
          </div>
        ))}
      </div>

      {!loading && filtered.length === 0 && (
        <p className="text-brand-brown/60">No entries. Try a broader term (e.g., “Bengal”).</p>
      )}
    </div>
  );
}
