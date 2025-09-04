from pydantic import BaseModel
try:
    # Pydantic v2
    from pydantic import ConfigDict
    _config = {"model_config": ConfigDict(from_attributes=True)}
except Exception:
    # Pydantic v1 fallback
    class _Cfg: orm_mode = True
    _config = {"Config": _Cfg}

class PerformanceOut(BaseModel):
    id: int
    title: str
    artist: str
    art_form: str
    year: int | None = None
    video_url: str
    tags: str | None = None
    rights_owner: str | None = None
    description: str | None = None
    # apply config for ORM -> Pydantic
    locals().update(_config)  # type: ignore

class RevivalOut(BaseModel):
    id: int
    name: str
    region: str | None = None
    status: str | None = None
    description: str | None = None
    references: str | None = None
    locals().update(_config)  # type: ignore
