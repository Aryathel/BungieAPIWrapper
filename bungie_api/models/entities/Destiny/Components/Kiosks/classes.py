from typing import (
    List,
    Mapping,
)

from arya_api_framework import BaseModel

from ... import Quests


__all__ = [
    'DestinyKiosksComponent',
]


class DestinyKioskItem(BaseModel):
    index: int
    canAcquire: bool
    failureIndexes: List[int]
    flavorObjective: Quests.DestinyObjectiveProgress


class DestinyKiosksComponent(BaseModel):
    kioskItems: Mapping[int, List[DestinyKioskItem]]
