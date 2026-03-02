"""
Stage-43.0 — Multi-Timeline Forecast API
Provides advisory future comparison endpoints.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List

from core.multitimeline_forecast import multi_timeline_forecast_engine

router = APIRouter(prefix="/forecast", tags=["Multi-Timeline Forecast"])


class TimelineCreate(BaseModel):
    scenario_name: str
    timelines: List[Dict[str, Any]]


class ForecastRun(BaseModel):
    timeline_set_id: str


@router.post("/create")
def create_timelines(data: TimelineCreate):
    return multi_timeline_forecast_engine.create_timelines(
        data.scenario_name,
        data.timelines,
    )


@router.post("/run")
def run_forecast(data: ForecastRun):
    result = multi_timeline_forecast_engine.run_forecast(
        data.timeline_set_id
    )

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result


@router.get("/{timeline_set_id}")
def get_timelines(timeline_set_id: str):
    result = multi_timeline_forecast_engine.get_timelines(
        timeline_set_id
    )

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result