from typing import (
    ForwardRef,
    List,
    Optional,
)

from arya_api_framework import BaseModel

from ....utils import ValidatedDatetime
from ..enums import BungieMembershipType
from .enums import (
    FireteamPlatform,
    FireteamPlatformInviteResult,
)


__all__ = [
    'FireteamSummary',
    'FireteamUserInfoCard',
    'FireteamMember',
    'FireteamResponse',
]


UserInfoCard = ForwardRef('User.UserInfoCard')


class FireteamSummary(BaseModel):
    fireteamId: int
    groupId: int
    platform: FireteamPlatform
    activityType: int
    isImmediate: bool
    scheduledTime: Optional[ValidatedDatetime]
    ownerMembershipId: int
    playerSlotCount: int
    alternateSlotCount: Optional[int]
    availablePlayerSlotCount: int
    availableAlternateSlotCount: int
    title: str
    dateCreated: ValidatedDatetime
    dateModified: Optional[ValidatedDatetime]
    isPublic: bool
    locale: str
    isValid: bool
    datePlayerModified: ValidatedDatetime
    titleBeforeModeration: Optional[str]


class FireteamUserInfoCard(BaseModel):
    FireteamDisplayName: str
    FireteamMembershipType: int
    supplementalDisplayName: Optional[str]
    iconPath: str
    crossSaveOverride: BungieMembershipType
    applicableMembershipTypes: List[BungieMembershipType]
    isPublic: bool
    membershipType: BungieMembershipType
    membershipId: int
    displayName: str
    bungieGlobalDisplayName: Optional[str]
    bungieGlobalDisplayNameCode: Optional[int]


class FireteamMember(BaseModel):
    destinyUserInfo: FireteamUserInfoCard
    bungieNetUserInfo: UserInfoCard
    characterId: int
    dateJoined: ValidatedDatetime
    hasMicrophone: bool
    lastPlatformInviteAttemptDate: ValidatedDatetime
    lastPlatformInviteAttemptResult: FireteamPlatformInviteResult


class FireteamResponse(BaseModel):
    Summary: FireteamSummary
    Members: List[FireteamMember]
    Alternates: List[FireteamMember]


from .. import User
