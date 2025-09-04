# backend/scripts/expand_tags.py
# Purpose: read backend/data/performances_seed.csv, enrich tags based on art_form,
# and write back a new CSV with improved tags.

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # -> Kala/
CSV_IN = ROOT / "backend" / "data" / "performances_seed.csv"
CSV_OUT = ROOT / "backend" / "data" / "performances_seed_enriched.csv"

# Simple synonym packs per art form (extend anytime)
ART_SYNS = {
    "bharatanatyam": [
        "bharatanatyam", "bharatnatyam", "bharatham",
        "classical dance", "tamil nadu", "carnatic"
    ],
    "odissi": [
        "odissi", "odishi",
        "classical dance", "odisha", "jagannath"
    ],
    "kathak": [
        "kathak", "kathhak",
        "classical dance", "hindustani", "chakkars", "tatkar"
    ],
    "kuchipudi": [
        "kuchipudi", "kuchipoodi",
        "classical dance", "andhra pradesh", "yakshagana"
    ],
    "mohiniyattam": [
        "mohiniyattam", "mohiniattam",
        "classical dance", "kerala", "sopana"
    ],
    "manipuri": [
        "manipuri",
        "classical dance", "raslila", "manipur"
    ],
    "kathakali": [
        "kathakali",
        "dance drama", "kerala", "chenda", "maddalam"
    ],
    "sattriya": [
        "sattriya",
        "classical dance", "assam", "vaishnavite"
    ],
}

def normalize(s: str) -> str:
    return (s or "").strip()

def merge_tags(existing: str, extra: list[str]) -> str:
    base = [t.strip() for t in (existing or "").split(",") if t.strip()]
    merged = set([t.lower() for t in base])
    for t in extra:
        merged.add(t.lower())
    return ", ".join(sorted(merged))

def main():
    if not CSV_IN.exists():
        raise SystemExit(f"Missing: {CSV_IN}")
    df = pd.read_csv(CSV_IN)

    required = {"title", "artist", "art_form", "year", "video_url", "tags"}
    if not required.issubset(df.columns):
        raise SystemExit(f"{CSV_IN} must have columns: {required}")

    enriched = df.copy()
    for i, row in enriched.iterrows():
        af = normalize(str(row.get("art_form", ""))).lower()
        base_tags = row.get("tags", "")
        pack = []
        for key, words in ART_SYNS.items():
            if key in af:
                pack.extend(words)
        if pack:
            enriched.at[i, "tags"] = merge_tags(base_tags, pack)

    enriched.to_csv(CSV_OUT, index=False)
    print(f"Saved enriched tags → {CSV_OUT}")
    print("Done ✓")

if __name__ == "__main__":
    main()
