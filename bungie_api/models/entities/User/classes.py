from typing import (
    List,
    ForwardRef,
    Optional,
    Union,
)

from arya_api_framework import BaseModel

from ....utils import ValidatedDatetime
from ..Ignores import IgnoreResponse
from ..enums import BungieMembershipType


__all__ = [
    'UserInfoCard',
    'GeneralUser',
    'UserToUserContext',
    'UserMembershipData',
    'HardLinkedUserMembership',
    'UserSearchResponseDetail',
    'UserSearchResponse',
    'UserMembership',
]


GroupUserInfoCard = ForwardRef('GroupsV2.GroupUserInfoCard')


class UserInfoCard(BaseModel):
    supplementalDisplayName: Optional[str]
    iconPath: Optional[str]
    crossSaveOverride: int
    applicableMembershipTypes: Optional[List[BungieMembershipType]]
    isPublic: bool
    membershipType: BungieMembershipType
    membershipId: int
    displayName: Optional[str]
    bungieGlobalDisplayName: Optional[str]
    bungieGlobalDisplayNameCode: Optional[int]


class UserToUserContext(BaseModel):
    isFollowing: bool
    ignoreStatus: IgnoreResponse
    globalIgnoreEndDate: Optional[ValidatedDatetime]


class GeneralUser(BaseModel):
    membershipId: int
    uniqueName: str
    normalizedName: Optional[str]
    displayName: str
    profilePicture: int
    profileTheme: int
    userTitle: int
    successMessageFlags: int
    isDeleted: bool
    about: str
    firstAccess: Optional[ValidatedDatetime]
    lastUpdate: Optional[ValidatedDatetime]
    legacyPortalUID: Optional[int]
    context: Optional[UserToUserContext]
    psnDisplayName: Optional[str]
    xboxDisplayName: Optional[str]
    fbDisplayName: Optional[str]
    showActivity: Optional[bool]
    locale: str
    localeInheritDefault: bool
    lastBanReportId: Optional[int]
    showGroupMessaging: bool
    profilePicturePath: str
    profilePictureWidePath: Optional[str]
    profileThemeName: str
    userTitleDisplay: str
    statusText: str
    statusDate: ValidatedDatetime
    profileBanExpire: Optional[ValidatedDatetime]
    blizzardDisplayName: Optional[str]
    steamDisplayName: Optional[str]
    stadiaDisplayName: Optional[str]
    twitchDisplayName: Optional[str]
    cachedBungieGlobalDisplayName: Optional[str]
    cachedBungieGlobalDisplayNameCode: Optional[int]


class UserMembershipData(BaseModel):
    destinyMemberships: List[GroupUserInfoCard]
    primaryMembershipId: Optional[int]
    bungieNetUser: GeneralUser


class UserMembership(BaseModel):
    membershipType: BungieMembershipType
    membershipId: int
    displayName: Optional[str]
    bungieGlobalDisplayName: Optional[str]
    bungieGlobalDisplayNameCode: Optional[int]


class HardLinkedUserMembership(BaseModel):
    membershipType: BungieMembershipType
    membershipId: int
    CrossSaveOverriddenType: BungieMembershipType
    CrossSaveOverriddenMembershipId: Optional[int]


class UserSearchResponseDetail(BaseModel):
    bungieGlobalDisplayName: str
    bungieGlobalDisplayNameCode: Optional[int]
    bungieNetMembershipId: Optional[int]
    destinyMemberships: List[UserInfoCard]


class UserSearchResponse(BaseModel):
    searchResults: List[UserSearchResponseDetail]
    page: int
    hasMore: bool


from .. import GroupsV2
