import pandas as pd
from sqlalchemy.orm import Session
from backend.db import Base, engine, SessionLocal
from backend.models import Performance, RevivalForm

PERF_CSV = "backend/data/performances_seed.csv"
REVIVAL_CSV = "backend/data/revival_seed.csv"

def seed_performances(db: Session):
    df = pd.read_csv(PERF_CSV)
    db.query(Performance).delete()
    items = []
    for _, r in df.iterrows():
        items.append(Performance(
            title=str(r["title"]),
            artist=str(r["artist"]),
            art_form=str(r["art_form"]),
            year=int(r["year"]) if pd.notna(r["year"]) else None,
            video_url=str(r["video_url"]),
            tags=str(r["tags"]) if pd.notna(r["tags"]) else None,
            rights_owner=str(r["rights_owner"]) if pd.notna(r["rights_owner"]) else None,
            description=str(r["description"]) if pd.notna(r["description"]) else None,
        ))
    db.add_all(items)
    db.commit()
    print(f"Seeded {len(items)} performances.")

def seed_revival(db: Session):
    df = pd.read_csv(REVIVAL_CSV)
    db.query(RevivalForm).delete()
    items = []
    for _, r in df.iterrows():
        items.append(RevivalForm(
            name=str(r["name"]),
            region=str(r["region"]) if pd.notna(r["region"]) else None,
            status=str(r["status"]) if pd.notna(r["status"]) else None,
            description=str(r["description"]) if pd.notna(r["description"]) else None,
            references=str(r["references"]) if pd.notna(r["references"]) else None,
        ))
    db.add_all(items)
    db.commit()
    print(f"Seeded {len(items)} revival forms.")

if __name__ == "__main__":
    # create tables
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        seed_performances(db)
        seed_revival(db)
    print("Done ✓")