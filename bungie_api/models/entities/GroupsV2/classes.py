from typing import (
    Dict,
    ForwardRef,
    List,
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel

from ....utils import ValidatedDatetime
from .. import Destiny, Queries, Exceptions
from ..enums import BungieMembershipType
from .enums import (
    GroupType,
    HostGuidedGamesPermissionLevel,
    ChatSecuritySetting,
    GroupApplicationResolveState,
)


__all__ = [
    'GroupUserInfoCard',
    'GroupResponse',
    'GroupFeatures',
    'ClanBanner',
    'GroupV2',
    'GroupV2ClanInfoAndInvestment',
    'GroupMember',
    'GroupPotentialMember',
    'GroupV2Card',
    'GroupV2ClanInfo',
    'GroupSearchResponse',
    'GroupOptionalConversation',
    'SearchResultOfGroupMember',
    'GroupMemberLeaveResult',
    'GroupBan',
    'SearchResultOfGroupBan',
    'GroupMemberApplication',
    'SearchResultOfGroupMemberApplication',
    'GroupMembership',
    'GetGroupsForMemberResponse',
    'GroupMembershipSearchResponse',
    'GroupApplicationResponse',
]


UserInfoCard = ForwardRef('User.UserInfoCard')


class GroupUserInfoCard(BaseModel):
    LastSeenDisplayName: str
    LastSeenDisplayNameType: BungieMembershipType
    supplementalDisplayName: Optional[str]
    iconPath: str
    crossSaveOverride: int
    applicableMembershipTypes: List[BungieMembershipType]
    isPublic: bool
    membershipType: BungieMembershipType
    membershipId: int
    displayName: str
    bungieGlobalDisplayName: str
    bungieGlobalDisplayNameCode: Optional[str]


class GroupFeatures(BaseModel):
    maximumMembers: int
    maximumMembershipsOfGroupType: int
    capabilities: int
    membershipTypes: List[BungieMembershipType]
    invitePermissionOverride: bool
    updateCulturePermissionOverride: bool
    hostGuidedGamePermissionOverride: HostGuidedGamesPermissionLevel
    updateBannerPermissionOverride: bool
    joinLevel: int


class ClanBanner(BaseModel):
    decalId: int
    decalColorId: int
    decalBackgroundColorId: int
    gonfalonId: int
    gonfalonColorId: int
    gonfalonDetailId: int
    gonfalonDetailColorId: int


class GroupV2ClanInfoAndInvestment(BaseModel):
    d2ClanProgressions: Dict[int, Destiny.DestinyProgression]
    clanCallsign: str
    clanBannerData: ClanBanner


class GroupV2(BaseModel):
    groupId: int
    name: str
    groupType: GroupType
    membershipIdCreated: int
    creationDate: ValidatedDatetime
    modificationDate: ValidatedDatetime
    about: str
    tags: List[str]
    memberCount: int
    isPublic: bool
    isPublicTopicAdminOnly: bool
    motto: str
    allowChat: bool
    isDefaultPostPublic: bool
    chatSecurity: int
    locale: str
    avatarImageIndex: int
    homepage: int
    membershipOption: int
    defaultPublicity: int
    theme: str
    bannerPath: str
    avatarPath: str
    conversationId: int
    enableInvitationMessagingForAdmins: bool
    banExpireDate: Optional[ValidatedDatetime]
    features: GroupFeatures
    clanInfo: GroupV2ClanInfoAndInvestment


class GroupMember(BaseModel):
    memberType: int
    isOnline: bool
    lastOnlineStatusChange: int
    groupId: int
    destinyUserInfo: GroupUserInfoCard
    bungieNetUserInfo: Optional[UserInfoCard]
    joinDate: ValidatedDatetime


class GroupPotentialMember(BaseModel):
    potentialStatus: int
    groupId: int
    destinyUserInfo: GroupUserInfoCard
    bungieNetUserInfo: UserInfoCard
    joinDate: ValidatedDatetime


class GroupResponse(BaseModel):
    detail: GroupV2
    founder: GroupMember
    alliedIds: List[int]
    parentGroup: Optional[GroupV2]
    allianceStatus: int
    groupJoinInviteCount: int
    currentUserMembershipsInactiveForDestiny: bool
    currentUserMemberMap: Mapping[str, GroupMember]
    currentUserPotentialMemberMap: Mapping[int, GroupPotentialMember]


class GroupV2ClanInfo(BaseModel):
    clanCallsign: str
    clanBannerData: ClanBanner


class GroupV2Card(BaseModel):
    groupId: int
    name: str
    groupType: GroupType
    creationDate: ValidatedDatetime
    about: str
    motto: str
    memberCount: int
    locale: str
    membershipOption: int
    capabilities: int
    clanInfo: GroupV2ClanInfo
    avatarPath: str
    theme: str


class GroupSearchResponse(BaseModel):
    results: List[GroupV2Card]
    totalResults: int
    hasMore: bool
    query: Queries.PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool


class GroupOptionalConversation(BaseModel):
    groupId: int
    conversationId: int
    chatEnabled: bool
    chatName: str
    chatSecurity: ChatSecuritySetting


class SearchResultOfGroupMember(BaseModel):
    results: List[GroupMember]
    totalResults: int
    hasMore: bool
    query: Queries.PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool


class GroupMemberLeaveResult(BaseModel):
    group: GroupV2
    groupDeleted: bool


class GroupBan(BaseModel):
    groupId: int
    lastModifiedBy: UserInfoCard
    createdBy: UserInfoCard
    dateBanned: ValidatedDatetime
    dateExpires: ValidatedDatetime
    comment: str
    bungieNetUserInfo: Optional[UserInfoCard]
    destinyUserInfo: GroupUserInfoCard


class SearchResultOfGroupBan(BaseModel):
    results: List[GroupBan]
    totalResults: int
    hasMore: bool
    query: Queries.PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool


class GroupMemberApplication(BaseModel):
    groupId: int
    creationDate: ValidatedDatetime
    resolveState: GroupApplicationResolveState
    resolveDate: Optional[ValidatedDatetime]
    resolveByMembershipId: Optional[int]
    requestMessage: Optional[str]
    resolveMessage: Optional[str]
    destinyUserInfo: GroupUserInfoCard
    bungieNetUserInfo: Optional[UserInfoCard]


class SearchResultOfGroupMemberApplication(BaseModel):
    results: List[GroupMemberApplication]
    totalResults: int
    hasMore: bool
    query: Queries.PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool


class GroupMembership(BaseModel):
    member: GroupMember
    group: GroupV2


class GetGroupsForMemberResponse(BaseModel):
    areAllMembershipsInactive: Optional[Dict[int, bool]]
    results: List[GroupMembership]
    totalResults: int
    hasMore: bool
    query: Queries.PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool


class GroupMembershipSearchResponse(BaseModel):
    results: List[GroupMembership]
    totalResults: int
    hasMore: bool
    query: Queries.PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool


class GroupApplicationResponse(BaseModel):
    resolution: Exceptions.PlatformErrorCodes


from .. import User
