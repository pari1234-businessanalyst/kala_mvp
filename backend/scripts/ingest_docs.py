# backend/scripts/ingest_docs.py
import re
import pickle
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

DOCS_DIR = Path("backend/data/docs")
ART_VEC = Path("backend/data/retriever_vectorizer.pkl")
ART_MAT = Path("backend/data/retriever_matrix.pkl")
ART_IDX = Path("backend/data/doc_index.csv")

def load_docs() -> pd.DataFrame:
    """Read all .md files, split on blank lines into short paragraphs."""
    rows = []
    for p in DOCS_DIR.glob("*.md"):
        text = p.read_text(encoding="utf-8", errors="ignore")
        # split on blank lines
        chunks = [c.strip() for c in re.split(r"\n\s*\n", text) if c.strip()]
        for i, c in enumerate(chunks):
            rows.append({"doc_path": str(p.name), "para_id": i, "text": c})
    return pd.DataFrame(rows)

if __name__ == "__main__":
    if not DOCS_DIR.exists():
        raise SystemExit(f"Docs folder not found: {DOCS_DIR}")

    df = load_docs()
    if df.empty:
        raise SystemExit(f"No .md files found in {DOCS_DIR}. Add notes and retry.")

    # Build TF-IDF (unigrams + bigrams is good for short notes)
    vec = TfidfVectorizer(ngram_range=(1, 2), min_df=1, max_df=0.95)
    X = vec.fit_transform(df["text"])

    # Save artifacts
    ART_VEC.parent.mkdir(parents=True, exist_ok=True)
    pickle.dump(vec, open(ART_VEC, "wb"))
    pickle.dump(X, open(ART_MAT, "wb"))
    df.to_csv(ART_IDX, index=False)

    print(f"Ingested {len(df)} passages from {DOCS_DIR}.")
    print(f"Saved: {ART_VEC.name}, {ART_MAT.name}, {ART_IDX.name}")
