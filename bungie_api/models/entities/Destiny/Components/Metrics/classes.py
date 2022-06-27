from typing import Mapping

from arya_api_framework import BaseModel

from ... import Quests


__all__ = [
    'DestinyMetricComponent',
    'DestinyMetricsComponent',
]


class DestinyMetricComponent(BaseModel):
    invisible: bool
    objectiveProgress: Quests.DestinyObjectiveProgress


class DestinyMetricsComponent(BaseModel):
    metrics: Mapping[int, DestinyMetricComponent]
    metricsRootNodeHash: int
