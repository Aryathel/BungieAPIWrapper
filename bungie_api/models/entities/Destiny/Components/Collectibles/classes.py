from typing import (
    List,
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel

from ... import DestinyCollectibleState


__all__ = [
    'DestinyCollectibleComponent',
    'DestinyCollectiblesComponent',
    'DestinyProfileCollectiblesComponent',
]


class DestinyCollectibleComponent(BaseModel):
    state: DestinyCollectibleState


class DestinyCollectiblesComponent(BaseModel):
    collectibles: Mapping[int, DestinyCollectibleComponent]
    collectionCategoriesRootNodeHash: int
    collectionBadgesRootNodeHash: int


class DestinyProfileCollectiblesComponent(BaseModel):
    recentCollectibleHashes: List[int]
    newnessFlaggedCollectibleHashes: Optional[List[int]]
    collectibles: Mapping[int, DestinyCollectibleComponent]
    collectionCategoriesRootNodeHash: int
    collectionBadgesRootNodeHash: int
