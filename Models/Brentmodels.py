from pydantic import BaseModel

class SeasonalTip(BaseModel):
    id: int
    title: str
    content: str
    season: str