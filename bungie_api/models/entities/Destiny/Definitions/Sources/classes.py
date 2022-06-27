from typing import (
    Dict,
    ForwardRef,
    List,
)

from arya_api_framework import BaseModel


__all__ = [
    'DestinyItemSourceDefinition',
]


DestinyInventoryItemStatDefinition = ForwardRef('Definitions.DestinyInventoryItemStatDefinition')


class DestinyItemSourceDefinition(BaseModel):
    level: int
    minQuality: int
    maxQuality: int
    minLevelRequired: int
    maxLevelRequired: int
    computedStats: Dict[int, DestinyInventoryItemStatDefinition]
    sourceHashes: List[int]


from ... import Definitions
