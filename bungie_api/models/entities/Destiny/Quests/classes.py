from typing import (
    List,
    Optional,
)

from arya_api_framework import BaseModel


__all__ = [
    'DestinyObjectiveProgress',
    'DestinyQuestStatus',
]


class DestinyObjectiveProgress(BaseModel):
    objectiveHash: int
    destinationHash: Optional[int]
    activityHash: Optional[int]
    progress: Optional[int]
    completionValue: int
    complete: bool
    visible: bool


class DestinyQuestStatus(BaseModel):
    questHash: int
    stepHash: int
    stepObjectives: List[DestinyObjectiveProgress]
    tracked: bool
    itemInstanceId: int
    completed: bool
    redeemed: bool
    started: bool
    vendorHash: Optional[int]
