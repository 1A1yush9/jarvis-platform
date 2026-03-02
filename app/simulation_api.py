"""
Stage-42.0 — Strategic Simulation API

Allows controlled hypothetical simulations.
No operational execution allowed.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

from core.strategic_simulation_sandbox import strategic_simulation_sandbox

router = APIRouter(prefix="/simulation", tags=["Strategic Simulation"])


class ScenarioCreate(BaseModel):
    name: str
    assumptions: Dict[str, Any]


class ScenarioRun(BaseModel):
    scenario_id: str


@router.post("/create")
def create_scenario(data: ScenarioCreate):
    return strategic_simulation_sandbox.create_scenario(
        data.name,
        data.assumptions,
    )


@router.post("/run")
def run_simulation(data: ScenarioRun):
    result = strategic_simulation_sandbox.run_simulation(
        data.scenario_id
    )

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result


@router.get("/{scenario_id}")
def get_scenario(scenario_id: str):
    result = strategic_simulation_sandbox.get_scenario(scenario_id)

    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])

    return result