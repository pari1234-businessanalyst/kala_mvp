from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import or_

from .db import Base, engine, SessionLocal
from .models import Performance, RevivalForm
from .schemas import PerformanceOut, RevivalOut
# add these to your existing imports at the top of backend/main.py
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from fastapi import Body


# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kala API (MVP)")

# ---- Ask Kala: load retriever artifacts ----
VEC_PATH = "backend/data/retriever_vectorizer.pkl"
MAT_PATH = "backend/data/retriever_matrix.pkl"
IDX_PATH = "backend/data/doc_index.csv"

try:
    _vectorizer = pickle.load(open(VEC_PATH, "rb"))
    _matrix = pickle.load(open(MAT_PATH, "rb"))
    _doc_index = pd.read_csv(IDX_PATH)
    _retriever_ready = True
    print("Retriever ready ✓")
except Exception as e:
    print("Retriever not ready:", e)
    _vectorizer = None
    _matrix = None
    _doc_index = None
    _retriever_ready = False


# Allow all origins for MVP (so your React frontend can call it)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---- Performances ----
@app.get("/api/performances", response_model=list[PerformanceOut])
def list_performances(
    q: str | None = Query(None, description="Search in title/artist/tags"),
    art_form: str | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Performance)
    if q:
        like = f"%{q}%"
        query = query.filter(
            or_(
                Performance.title.like(like),
                Performance.artist.like(like),
                Performance.tags.like(like)
            )
        )
    if art_form:
        query = query.filter(Performance.art_form == art_form)
    return query.order_by(Performance.year.desc()).limit(100).all()

@app.get("/api/performances/{perf_id}", response_model=PerformanceOut)
def get_performance(perf_id: int, db: Session = Depends(get_db)):
    row = db.query(Performance).filter(Performance.id == perf_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Performance not found")
    return row

# ---- Revival ----
@app.get("/api/revival", response_model=list[RevivalOut])
def list_revival(
    region: str | None = Query(None),
    status: str | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(RevivalForm)
    if region:
        query = query.filter(RevivalForm.region == region)
    if status:
        query = query.filter(RevivalForm.status == status)
    return query.order_by(RevivalForm.name.asc()).limit(200).all()

@app.get("/api/revival/{item_id}", response_model=RevivalOut)
def get_revival(item_id: int, db: Session = Depends(get_db)):
    row = db.query(RevivalForm).filter(RevivalForm.id == item_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Revival item not found")
    return row

def retrieve_topk(query: str, k: int = 3):
    """Return top-k passages (as DataFrame) for the query."""
    qv = _vectorizer.transform([query])
    sims = cosine_similarity(qv, _matrix)[0]
    top_idx = sims.argsort()[::-1][:k]
    rows = _doc_index.iloc[top_idx].copy()
    rows["score"] = sims[top_idx]
    return rows

def synthesize(passages: list[dict], question: str) -> str:
    """Very simple synthesis: join top 1–2 snippets into a short answer."""
    if not passages:
        return "I couldn't find enough information. Please try another question."
    bits = [p["text"] for p in passages][:2]
    answer = " ".join(bits)
    # keep it short-ish
    return answer[:900]

@app.post("/api/ask")
def ask_kala(payload: dict = Body(...)):
    """Ask Kala: returns a short answer + the passages used."""
    if not _retriever_ready:
        return {"answer": "Knowledge base not ready. Please add docs and run ingest.", "passages": []}

    q = str(payload.get("query") or "").strip()
    if not q:
        return {"answer": "Please enter a question.", "passages": []}

    rows = retrieve_topk(q, k=3)
    passages = rows[["doc_path", "para_id", "text", "score"]].to_dict(orient="records")
    answer = synthesize(passages, q)
    return {"answer": answer, "passages": passages}
