from typing import (
    List,
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel

from .. import Exceptions
from . import (
    Challenges,
    Definitions,
)
from .enums import (
    DestinyActivityDifficultyTier,
    TalentNodeState,
    DestinyProgressionRewardItemState,
)


__all__ = [
    'DestinyProgression',
    'DestinyProgressionResetEntry',
    'DestinyItemQuantity',
    'DyeReference',
    'DestinyActivity',
    'DestinyStat',
    'DestinyTalentNodeStatBlock',
    'DestinyTalentNode',
    'DestinyUnlockStatus',
    'DestinyEquipItemResult',
    'DestinyEquipItemResults',
]


class DestinyProgressionResetEntry(BaseModel):
    season: int
    resets: int


class DestinyProgression(BaseModel):
    progressionHash: int
    dailyProgress: int
    dailyLimit: int
    weeklyProgress: int
    weeklyLimit: int
    currentProgress: int
    level: int
    levelCap: int
    stepIndex: int
    progressToNextLevel: int
    nextLevelAt: int
    currentResetCount: Optional[int]
    seasonResets: Optional[DestinyProgressionResetEntry]
    rewardItemStates: Optional[List[DestinyProgressionRewardItemState]]


class DestinyItemQuantity(BaseModel):
    itemHash: int
    itemInstanceId: Optional[int]
    quantity: int
    hasConditionalVisibility: bool


class DyeReference(BaseModel):
    channelHash: int
    dyeHash: int


class DestinyActivity(BaseModel):
    activityHash: int
    isNew: bool
    canLead: bool
    canJoin: bool
    isCompleted: bool
    isVisible: bool
    displayLevel: Optional[int]
    recommendedLight: Optional[int]
    difficultyTier: DestinyActivityDifficultyTier
    challenges: Optional[List[Challenges.DestinyChallengeStatus]]
    modifierHashes: Optional[List[int]]
    booleanActivityOptions: Optional[Mapping[int, bool]]
    loadoutRequirementIndex: Optional[int]


class DestinyStat(BaseModel):
    statHash: int
    value: int


class DestinyTalentNodeStatBlock(BaseModel):
    currentStepStats: List[DestinyStat]
    nextStepStats: List[DestinyStat]


class DestinyTalentNode(BaseModel):
    nodeIndex: int
    nodeHash: int
    state: TalentNodeState
    isActivated: bool
    stepIndex: int
    materialsToUpgrade: List[Definitions.DestinyMaterialRequirement]
    activationGridLevel: int
    progressPercent: int
    hidden: bool
    nodeStatsBlock: Optional[DestinyTalentNodeStatBlock]


class DestinyUnlockStatus(BaseModel):
    unlockHash: int
    isSet: bool


class DestinyEquipItemResult(BaseModel):
    itemInstanceId: int
    equipStatus: Exceptions.PlatformErrorCodes


class DestinyEquipItemResults(BaseModel):
    equipResults: List[DestinyEquipItemResult]
