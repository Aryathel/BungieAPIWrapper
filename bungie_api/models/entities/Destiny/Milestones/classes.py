from typing import (
    List,
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel

from .....utils import ValidatedDatetime
from .. import (
    Challenges,
    HistoricalStats,
    Quests,
)


__all__ = [
    'DestinyMilestoneActivity',
    'DestinyMilestoneQuest',
    'DestinyMilestoneActivityPhase',
    'DestinyMilestoneChallengeActivity',
    'DestinyMilestoneVendor',
    'DestinyMilestoneRewardEntry',
    'DestinyMilestoneRewardCategory',
    'DestinyMilestone',
]


class DestinyMilestoneActivity(BaseModel):
    activityHash: int
    activityModeHash: Optional[int]
    activityModeType: Optional[HistoricalStats.Definitions.DestinyActivityModeType]


class DestinyMilestoneQuest(BaseModel):
    questItemHash: int
    status: Quests.DestinyQuestStatus
    activity: Optional[DestinyMilestoneActivity]
    challenges: Optional[List[Challenges.DestinyChallengeStatus]]


class DestinyMilestoneActivityPhase(BaseModel):
    complete: bool
    phaseHash: int


class DestinyMilestoneChallengeActivity(BaseModel):
    activityHash: int
    challenges: List[Challenges.DestinyChallengeStatus]
    modifierHashes: Optional[List[int]]
    booleanActivityOptions: Optional[Mapping[int, bool]]
    loadoutRequirementsIndex: Optional[int]
    phases: Optional[List[DestinyMilestoneActivityPhase]]


class DestinyMilestoneVendor(BaseModel):
    vendorHash: int
    previewItemHash: Optional[int]


class DestinyMilestoneRewardEntry(BaseModel):
    rewardEntryHash: int
    earned: bool
    redeemed: bool


class DestinyMilestoneRewardCategory(BaseModel):
    rewardCategoryHash: int
    entries: List[DestinyMilestoneRewardEntry]


class DestinyMilestone(BaseModel):
    milestoneHash: int
    availableQuests: Optional[List[DestinyMilestoneQuest]]
    activities: Optional[List[DestinyMilestoneChallengeActivity]]
    values: Optional[Mapping[str, float]]
    vendorHashes: Optional[List[int]]
    vendors: Optional[List[DestinyMilestoneVendor]]
    rewards: Optional[List[DestinyMilestoneRewardCategory]]
    startDate: Optional[ValidatedDatetime]
    endDate: Optional[ValidatedDatetime]
    order: int
