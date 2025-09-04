# backend/scripts/ingest_notes.py
# Build a simple TF-IDF index from markdown notes in backend/notes/
# Outputs: backend/data/retriever_vectorizer.pkl, retriever_matrix.pkl, doc_index.csv

from pathlib import Path
import re
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

ROOT = Path(__file__).resolve().parents[2]  # points to Kala/
NOTES_DIR = ROOT / "backend" / "notes"
DATA_DIR = ROOT / "backend" / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

VEC_PATH = DATA_DIR / "retriever_vectorizer.pkl"
MAT_PATH = DATA_DIR / "retriever_matrix.pkl"
IDX_PATH = DATA_DIR / "doc_index.csv"

def read_markdown_paragraphs(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    # split by blank lines; keep only meaningful chunks
    raw_paras = re.split(r"\n\s*\n", text)
    paras = []
    for i, p in enumerate(raw_paras):
        p_clean = re.sub(r"\s+", " ", p).strip()
        if len(p_clean) >= 40:  # ignore tiny lines
            paras.append((i, p_clean))
    return paras

def main():
    if not NOTES_DIR.exists():
        raise SystemExit(f"Notes folder not found: {NOTES_DIR}")

    rows = []
    for md in sorted(NOTES_DIR.glob("*.md")):
        for para_id, para_text in read_markdown_paragraphs(md):
            rows.append({"doc_path": md.name, "para_id": para_id, "text": para_text})

    if not rows:
        raise SystemExit("No paragraphs found. Add some .md files to backend/notes/.")

    df = pd.DataFrame(rows)
    print(f"Loaded {len(df)} paragraphs from {len(df['doc_path'].unique())} files.")

    # Build TF-IDF
    vec = TfidfVectorizer(stop_words="english", ngram_range=(1,2), max_features=20000)
    X = vec.fit_transform(df["text"].values)

    # Save artifacts
    with open(VEC_PATH, "wb") as f:
        pickle.dump(vec, f)
    with open(MAT_PATH, "wb") as f:
        pickle.dump(X, f)
    df.to_csv(IDX_PATH, index=False)

    print(f"Saved vectorizer → {VEC_PATH}")
    print(f"Saved matrix     → {MAT_PATH}")
    print(f"Saved index      → {IDX_PATH}")
    print("Done ✓")

if __name__ == "__main__":
    main()
