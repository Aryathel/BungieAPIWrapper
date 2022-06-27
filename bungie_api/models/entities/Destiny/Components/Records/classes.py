from typing import (
    List,
    Mapping,
    Optional,
)


from arya_api_framework import BaseModel
from pydantic import Field


from ... import (
    DestinyRecordState,
    Quests
)


__all__ = [
    'DestinyRecordComponent',
    'DestinyRecordsComponent',
    'DestinyProfileRecordsComponent',
    'DestinyCharacterRecordsComponent',
]


class DestinyRecordComponent(BaseModel):
    state: DestinyRecordState
    objectives: Optional[List[Quests.DestinyObjectiveProgress]]
    intervalObjectives: Optional[List[Quests.DestinyObjectiveProgress]]
    intervalsRedeemedCount: int
    completedCount: Optional[int]
    rewardVisibility: Optional[List[bool]] = Field(alias='rewardVisibilty')


class DestinyRecordsComponent(BaseModel):
    records: Mapping[int, DestinyRecordComponent]
    recordCategoriesRootNodeHash: int
    recordSealsRootNodeHash: int


class DestinyProfileRecordsComponent(BaseModel):
    score: int
    activeScore: int
    legacyScore: int
    lifetimeScore: int
    trackedRecordHash: Optional[int]
    records: Mapping[int, DestinyRecordComponent]
    recordCategoriesRootNodeHash: int
    recordSealsRootNodeHash: int


class DestinyCharacterRecordsComponent(BaseModel):
    featuredRecordHashes: List[int]
    records: Mapping[int, DestinyRecordComponent]
    recordCategoriesRootNodeHash: int
    recordSealsRootNodeHash: int
