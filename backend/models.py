from sqlalchemy import Column, Integer, String, Text
from backend.db import Base

class Performance(Base):
    __tablename__ = "performances"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    artist = Column(String(120), nullable=False)
    art_form = Column(String(80), nullable=False)
    year = Column(Integer, nullable=True)
    video_url = Column(String(500), nullable=False)
    tags = Column(String(300), nullable=True)        # comma-separated
    rights_owner = Column(String(120), nullable=True)
    description = Column(Text, nullable=True)

class RevivalForm(Base):
    __tablename__ = "revival_forms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(160), nullable=False)
    region = Column(String(120), nullable=True)
    status = Column(String(60), nullable=True)       # e.g., endangered/rare/declining
    description = Column(Text, nullable=True)
    references = Column(Text, nullable=True)
