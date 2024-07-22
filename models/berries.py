from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Berry:
    name: str
    growth_time: int

    def from_dict(data: dict[str, Any]) -> 'Berry':
        try:
            return Berry(
                name=data['name'],
                growth_time=data['growth_time']
            )
        except KeyError:
            return None
