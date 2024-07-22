from collections import Counter
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ProcessingResult:
    min: int
    median: float
    max: int
    variance: float
    mean: float
    frequency: dict[int, int]

def compute_values_info(values: list[int]):
    array = np.asarray(values)

    return ProcessingResult(
        min=int(array.min()),
        median=float(np.median(array)),
        max=int(array.max()),
        variance=float(array.var()),
        mean=float(array.mean()),
        frequency=dict(Counter(values))
    )
