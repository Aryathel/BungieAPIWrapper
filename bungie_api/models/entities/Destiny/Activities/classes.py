from typing import List

from arya_api_framework import BaseModel

from .. import DestinyItemQuantity


__all__ = [
    'DestinyPublicActivityStatus',
]


class DestinyPublicActivityStatus(BaseModel):
    challengeObjectiveHashes: List[int]
    modifierHashes: List[int]
    rewardTooltipItems: List[DestinyItemQuantity]
