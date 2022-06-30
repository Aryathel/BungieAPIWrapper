from typing import (
    List,
    Optional,
)

from arya_api_framework import BaseModel

from ...enums import BungieMembershipType
from ... import User
from .enums import (
    PresenceStatus,
    PresenceOnlineStateFlags,
    FriendRelationshipState,
    PlatformFriendType,
)


__all__ = [
    'BungieFriend',
    'BungieFriendListResponse',
    'BungieFriendRequestListResponse',
    'PlatformFriendResponse',
]


class BungieFriend(BaseModel):
    lastSeenAsMembershipId: int
    lastSeenAsBungieMembershipType: BungieMembershipType
    bungieGlobalDisplayName: Optional[str]
    bungieGlobalDisplayNameCode: Optional[int]
    onlineStatus: PresenceStatus
    onlineTitle: PresenceOnlineStateFlags
    relationship: FriendRelationshipState
    bungieNetUser: User.GeneralUser


class BungieFriendListResponse(BaseModel):
    friends: List[BungieFriend]


class BungieFriendRequestListResponse(BaseModel):
    incomingRequests: List[BungieFriend]
    outgoingRequests: List[BungieFriend]


class PlatformFriend(BaseModel):
    platformDisplayName: str
    friendPlatform: PlatformFriendType
    destinyMembershipId: Optional[int]
    destinyMembershipType: Optional[BungieMembershipType]
    bungieNetMembershipId: Optional[int]
    bungieGlobalDisplayName: Optional[str]
    bungieGlobalDisplayNameCode: Optional[str]


class PlatformFriendResponse(BaseModel):
    itemsPerPage: int
    currentPage: int
    hasMore: bool
    platformFriends: List[PlatformFriend]
