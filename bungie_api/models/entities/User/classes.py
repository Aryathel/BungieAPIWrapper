from typing import (
    ForwardRef,
    List,
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel

from ....utils import ValidatedDatetime
from ..Ignores import IgnoreResponse
from ..enums import BungieMembershipType
from .enums import OptInFlags


__all__ = [
    'UserInfoCard',
    'GeneralUser',
    'UserToUserContext',
    'UserMembershipData',
    'HardLinkedUserMembership',
    'UserSearchResponseDetail',
    'UserSearchResponse',
    'UserMembership',
    'EMailSettingSubscriptionLocalization',
    'EmailSubscriptionDefinition',
    'EmailOptInDefinition',
    'EMailSettingLocalization',
    'EmailViewDefinitionSetting',
    'EmailViewDefinition',
    'EmailSettings',
]


GroupUserInfoCard = ForwardRef('GroupsV2.GroupUserInfoCard')


class UserInfoCard(BaseModel):
    supplementalDisplayName: Optional[str]
    iconPath: Optional[str]
    crossSaveOverride: BungieMembershipType
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


class EMailSettingSubscriptionLocalization(BaseModel):
    unknownUserDescription: str
    registeredUserDescription: str
    unregisteredUserDescription: str
    knownUserActionText: str
    title: str
    description: str


class EmailSubscriptionDefinition(BaseModel):
    name: str
    localization: Mapping[str, EMailSettingSubscriptionLocalization]
    value: int


class EmailOptInDefinition(BaseModel):
    name: str
    value: OptInFlags
    setByDefault: bool
    dependentSubscriptions: List[EmailSubscriptionDefinition]


class EMailSettingLocalization(BaseModel):
    title: str
    description: str


class EmailViewDefinitionSetting(BaseModel):
    name: str
    localization: Mapping[str, EMailSettingLocalization]
    setByDefault: bool
    optInAggregateValue: OptInFlags
    subscriptions: List[EmailSubscriptionDefinition]


class EmailViewDefinition(BaseModel):
    name: str
    viewSettings: List[EmailViewDefinitionSetting]


class EmailSettings(BaseModel):
    optInDefinitions: Mapping[str, EmailOptInDefinition]
    subscriptionDefinitions: Mapping[str, EmailSubscriptionDefinition]
    views: Mapping[str, EmailViewDefinition]


from .. import GroupsV2
