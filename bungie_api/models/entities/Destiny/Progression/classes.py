from typing import (
    List,
    Optional
)

from arya_api_framework import BaseModel

from .. import (
    DestinyProgressionResetEntry,
    DestinyProgressionRewardItemState,
)


__all__ = [
    'DestinyFactionProgression',
]


class DestinyFactionProgression(BaseModel):
    factionHash: int
    factionVendorIndex: int
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
    seasonResets: Optional[List[DestinyProgressionResetEntry]]
    rewardItemStates: Optional[List[DestinyProgressionRewardItemState]]
