from typing import List

from arya_api_framework import BaseModel

from .. import DyeReference


__all__ = [
    'DestinyCharacterCustomization',
    'DestinyCharacterPeerView',
    'DestinyItemPeerView',
]


class DestinyCharacterCustomization(BaseModel):
    personality: int
    face: int
    skinColor: int
    lipColor: int
    eyeColor: int
    hairColors: List[int]
    featureColors: List[int]
    decalColor: int
    wearHelmet: bool
    hairIndex: int
    featureIndex: int
    decalIndex: int


class DestinyItemPeerView(BaseModel):
    itemHash: int
    dyes: List[DyeReference]


class DestinyCharacterPeerView(BaseModel):
    equipment: List[DestinyItemPeerView]
