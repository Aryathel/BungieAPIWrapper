from typing import List

from arya_api_framework import BaseModel

from .. import DestinyProgression


__all__ = [
    'DestinyArtifactProfileScoped',
    'DestinyArtifactTierItem',
    'DestinyArtifactTier',
    'DestinyArtifactCharacterScoped',
]


class DestinyArtifactProfileScoped(BaseModel):
    artifactHash: int
    pointProgression: DestinyProgression
    pointsAcquired: int
    powerBonusProgression: DestinyProgression
    powerBonus: int


class DestinyArtifactTierItem(BaseModel):
    itemHash: int
    isActive: bool


class DestinyArtifactTier(BaseModel):
    tierHash: int
    isUnlocked: bool
    pointsToUnlock: int
    items: List[DestinyArtifactTierItem]


class DestinyArtifactCharacterScoped(BaseModel):
    artifactHash: int
    pointsUsed: int
    resetCount: int
    tiers: List[DestinyArtifactTier]
