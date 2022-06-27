from typing import (
    List,
    Optional,
)

from arya_api_framework import BaseModel

from .. import Quests


__all__ = [
    'DestinyItemPlugBase',
    'DestinyItemPlug',
]


class DestinyItemPlugBase(BaseModel):
    plugItemHash: int
    canInsert: bool
    enabled: bool
    insertFailIndexes: Optional[List[int]]
    enableFailIndexes: Optional[List[int]]


class DestinyItemPlug(DestinyItemPlugBase):
    plugObjectives: Optional[List[Quests.DestinyObjectiveProgress]]
