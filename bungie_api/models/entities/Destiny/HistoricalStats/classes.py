from typing import (
    ForwardRef,
    List,
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel

from .....utils import ValidatedDatetime
from ...enums import BungieMembershipType
from . import Definitions


__all__ = [
    'DestinyHistoricalStatsActivity',
    'DestinyHistoricalStatsValuePair',
    'DestinyHistoricalStatsValue',
    'DestinyPlayer',
    'DestinyHistoricalWeaponStats',
    'DestinyPostGameCarnageReportExtendedData',
    'DestinyPostGameCarnageReportEntry',
    'DestinyPostGameCarnageReportTeamEntry',
    'DestinyPostGameCarnageReportData',
    'DestinyLeaderboardEntry',
    'DestinyLeaderboard',
    'DestinyClanAggregateStat',
    'DestinyHistoricalStatsPeriodGroup',
    'DestinyHistoricalStatsByPeriod',
    'DestinyHistoricalStatsWithMerged',
    'DestinyHistoricalStatsPerCharacter',
    'DestinyHistoricalStatsAccountResult',
    'DestinyActivityHistoryResults',
    'DestinyHistoricalWeaponStatsData',
    'DestinyAggregateActivityStats',
    'DestinyAggregateActivityResults',
]


UserInfoCard = ForwardRef('User.UserInfoCard')


class DestinyHistoricalStatsActivity(BaseModel):
    referenceId: int
    directorActivityHash: int
    instanceId: int
    mode: Definitions.DestinyActivityModeType
    modes: List[Definitions.DestinyActivityModeType]
    isPrivate: bool
    membershipType: BungieMembershipType


class DestinyHistoricalStatsValuePair(BaseModel):
    value: float
    displayValue: str


class DestinyHistoricalStatsValue(BaseModel):
    statId: Optional[str]
    basic: DestinyHistoricalStatsValuePair
    pga: Optional[DestinyHistoricalStatsValuePair]
    weighted: Optional[DestinyHistoricalStatsValuePair]
    activityId: Optional[int]


class DestinyPlayer(BaseModel):
    destinyUserInfo: UserInfoCard
    characterClass: str
    classHash: int
    raceHash: int
    genderHash: int
    characterLevel: int
    lightLevel: int
    bungieNetUserInfo: Optional[UserInfoCard]
    clanName: Optional[str]
    clanTag: Optional[str]
    emblemHash: int


class DestinyHistoricalWeaponStats(BaseModel):
    referenceId: int
    values: Mapping[str, DestinyHistoricalStatsValue]


class DestinyPostGameCarnageReportExtendedData(BaseModel):
    weapons: List[DestinyHistoricalWeaponStats]
    values: Mapping[str, DestinyHistoricalStatsValue]


class DestinyPostGameCarnageReportEntry(BaseModel):
    standing: int
    score: DestinyHistoricalStatsValue
    player: DestinyPlayer
    characterId: int
    values: Mapping[str, DestinyHistoricalStatsValue]
    extended: DestinyPostGameCarnageReportExtendedData


class DestinyPostGameCarnageReportTeamEntry(BaseModel):
    teamId: int
    standing: DestinyHistoricalStatsValue
    score: DestinyHistoricalStatsValue
    teamName: str


class DestinyPostGameCarnageReportData(BaseModel):
    period: ValidatedDatetime
    startingPhaseIndex: Optional[int]
    activityWasStartedFromBeginning: Optional[bool]
    activityDetails: DestinyHistoricalStatsActivity
    entries: List[DestinyPostGameCarnageReportEntry]
    teams: List[DestinyPostGameCarnageReportTeamEntry]


class DestinyLeaderboardEntry(BaseModel):
    rank: int
    player: DestinyPlayer
    characterId: int
    value: DestinyHistoricalStatsValue


class DestinyLeaderboard(BaseModel):
    statId: str
    entries: List[DestinyLeaderboardEntry]


class DestinyClanAggregateStat(BaseModel):
    mode: Definitions.DestinyActivityModeType
    statId: str
    value: DestinyHistoricalStatsValue


class DestinyHistoricalStatsPeriodGroup(BaseModel):
    period: ValidatedDatetime
    activityDetails: Optional[DestinyHistoricalStatsActivity]
    values: Mapping[str, DestinyHistoricalStatsValue]


class DestinyHistoricalStatsByPeriod(BaseModel):
    allTime: Optional[Mapping[str, DestinyHistoricalStatsValue]]
    allTimeTier1: Optional[Mapping[str, DestinyHistoricalStatsValue]]
    allTimeTier2: Optional[Mapping[str, DestinyHistoricalStatsValue]]
    allTimeTier3: Optional[Mapping[str, DestinyHistoricalStatsValue]]
    daily: Optional[List[DestinyHistoricalStatsPeriodGroup]]
    monthly: Optional[List[DestinyHistoricalStatsPeriodGroup]]


class DestinyHistoricalStatsWithMerged(BaseModel):
    results: Mapping[str, DestinyHistoricalStatsByPeriod]
    merged: DestinyHistoricalStatsByPeriod


class DestinyHistoricalStatsPerCharacter(BaseModel):
    characterId: int
    deleted: bool
    results: Mapping[str, DestinyHistoricalStatsByPeriod]
    merged: DestinyHistoricalStatsByPeriod


class DestinyHistoricalStatsAccountResult(BaseModel):
    mergedDeletedCharacters: DestinyHistoricalStatsWithMerged
    mergedAllCharacters: DestinyHistoricalStatsWithMerged
    characters: List[DestinyHistoricalStatsPerCharacter]


class DestinyActivityHistoryResults(BaseModel):
    activities: List[DestinyHistoricalStatsPeriodGroup]


class DestinyHistoricalWeaponStatsData(BaseModel):
    weapons: List[DestinyHistoricalWeaponStats]


class DestinyAggregateActivityStats(BaseModel):
    activityHash: int
    values: Mapping[str, DestinyHistoricalStatsValue]


class DestinyAggregateActivityResults(BaseModel):
    activities: List[DestinyAggregateActivityStats]


from ... import User
