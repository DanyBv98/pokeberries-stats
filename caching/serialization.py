import pickle
from typing import Any


def serialize(obj: Any) -> bytes:
    return pickle.dumps(obj)

def deserialize(data: bytes) -> Any:
    return pickle.loads(data)
