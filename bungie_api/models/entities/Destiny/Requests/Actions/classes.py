from typing import (
    List,
    Optional,
)

from arya_api_framework import BaseModel

from ....enums import BungieMembershipType
from .enums import DestinySocketArrayType


__all__ = [
    'DestinyPostmasterTransferRequest',
    'DestinyItemActionRequest',
    'DestinyItemSetActionRequest',
    'DestinyItemStateRequest',
    'DestinyInsertPlugsRequestEntry',
    'DestinyInsertPlugsActionRequest',
    'DestinyInsertPlugsFreeActionRequest',
]


class DestinyPostmasterTransferRequest(BaseModel):
    itemReferenceHash: int
    stackSize: Optional[int]
    itemId: int
    characterId: int
    membershipType: BungieMembershipType


class DestinyItemActionRequest(BaseModel):
    itemId: int
    characterId: int
    membershipType: BungieMembershipType


class DestinyItemSetActionRequest(BaseModel):
    itemIds: List[int]
    characterId: int
    membershipType: BungieMembershipType


class DestinyItemStateRequest(BaseModel):
    state: bool
    itemId: int
    characterId: int
    membershipType: BungieMembershipType


class DestinyInsertPlugsRequestEntry(BaseModel):
    socketIndex: int
    socketArrayType: DestinySocketArrayType
    plugItemHash: int


class DestinyInsertPlugsActionRequest(BaseModel):
    actionToken: str
    itemInstanceId: int
    plug: DestinyInsertPlugsRequestEntry
    characterId: int
    membershipType: BungieMembershipType


class DestinyInsertPlugsFreeActionRequest(BaseModel):
    plug: DestinyInsertPlugsRequestEntry
    itemId: int
    characterId: int
    membershipType: BungieMembershipType
