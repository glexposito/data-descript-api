from pydantic import BaseModel, Field


class Dataset(BaseModel):
    data: list[float] = Field(min_items=1, max_items=10000)


class Stats(BaseModel):
    mean: float
    median: float
    variance: float | None
    standard_deviation: float | None
    min: float
    max: float
    range: float
    q1: float
    q2: float
    q3: float
