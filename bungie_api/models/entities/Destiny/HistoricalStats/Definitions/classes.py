from typing import (
    List,
    Optional,
)

from arya_api_framework import BaseModel

from .enums import (
    DestinyActivityModeType,
    PeriodType,
    DestinyStatsCategoryType,
    UnitType,
    DestinyStatsMergeMethod,
)


__all__ = [
    'DestinyHistoricalStatsDefinition',
]


class DestinyHistoricalStatsDefinition(BaseModel):
    statId: str
    group: int
    periodTypes: List[PeriodType]
    modes: List[DestinyActivityModeType]
    category: DestinyStatsCategoryType
    statName: str
    statNameAbbr: Optional[str]
    statDescription: Optional[str]
    unitType: UnitType
    iconImage: Optional[str]
    mergeMethod: Optional[DestinyStatsMergeMethod]
    unitLabel: str
    weight: int
    medalTierIdentifier: Optional[str]
    contentIconOverrideId: Optional[str]
    medalTierHash: Optional[int]
    bestActivityIdPropertyName: Optional[str]
