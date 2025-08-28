from fastapi import APIRouter
from queries.Brentqueries import get_all_tips_query, get_tips_by_season_query
from Models.Brentmodels import SeasonalTip

router = APIRouter()

@router.get("/tips/all", response_model=list[SeasonalTip])
async def get_all_tips():
    tips = get_all_tips_query()
    return tips

@router.get("/tips/by_season", response_model=list[SeasonalTip])
async def get_tips_by_season(season: str):
    tips = get_tips_by_season_query(season)
    return tips