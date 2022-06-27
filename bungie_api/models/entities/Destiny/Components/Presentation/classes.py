from typing import (
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel

from ... import (
    DestinyPresentationNodeState,
    Quests
)


__all__ = [
    'DestinyPresentationNodeComponent',
    'DestinyPresentationNodesComponent',
]


class DestinyPresentationNodeComponent(BaseModel):
    state: DestinyPresentationNodeState
    objective: Optional[Quests.DestinyObjectiveProgress]
    progressValue: int
    completionValue: int
    recordCategoryScore: Optional[int]


class DestinyPresentationNodesComponent(BaseModel):
    nodes: Mapping[int, DestinyPresentationNodeComponent]
