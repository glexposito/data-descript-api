import numpy as np
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from models import Dataset, Stats
from utils import app


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.errors()},
    )


@app.post("/descriptive", response_model=Stats)
async def descriptive_statistics(dataset: Dataset):
    data = dataset.data

    variance = np.var(data, ddof=1)
    standard_deviation = np.std(data, ddof=1)

    if np.isnan(variance):
        variance = None
        standard_deviation = None

    stats = {
        "mean": np.mean(data),
        "median": np.median(data),
        "variance": variance,
        "standard_deviation": standard_deviation,
        "min": np.min(data),
        "max": np.max(data),
        "range": np.ptp(data),
        "q1": np.percentile(data, 25),
        "q2": np.percentile(data, 50),
        "q3": np.percentile(data, 75),
    }

    return stats
