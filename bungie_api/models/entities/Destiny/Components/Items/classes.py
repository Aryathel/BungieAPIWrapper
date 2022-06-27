from typing import (
    List,
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel

from ... import Quests


__all__ = [
    'DestinyItemPlugObjectivesComponent',
    'DestinyItemPlugComponent',
    'DestinyItemReusablePlugsComponent',
]


class DestinyItemPlugObjectivesComponent(BaseModel):
    objectivesPerPlug: Mapping[int, List[Quests.DestinyObjectiveProgress]]


class DestinyItemPlugComponent(BaseModel):
    plugObjectives: Optional[List[Quests.DestinyObjectiveProgress]]
    plugItemHash: int
    canInsert: int
    enabled: bool
    insertFailIndexes: Optional[List[int]]
    enableFailIndexes: Optional[List[int]]


class DestinyItemReusablePlugsComponent(BaseModel):
    plugs: Mapping[int, List[DestinyItemPlugComponent]]
