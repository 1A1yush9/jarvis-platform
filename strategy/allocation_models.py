from pydantic import BaseModel


class ResourceAllocation(BaseModel):
    stabilization_weight: float
    optimization_weight: float
    expansion_weight: float
