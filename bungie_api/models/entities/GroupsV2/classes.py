from typing import (
    Dict,
    ForwardRef,
    List,
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel

from ....utils import ValidatedDatetime
from .. import (
    Destiny,
    Queries,
)
from ..enums import BungieMembershipType
from .enums import (
    GroupType,
    HostGuidedGamesPermissionLevel,
    ChatSecuritySetting,
    GroupApplicationResolveState,
    MembershipOption,
    Capabilities,
    GroupDateRange,
    GroupSortBy,
    GroupMemberCountFilter,
    AllianceStatus,
    GroupHomepage,
    GroupPostPublicity,
    RuntimeGroupMemberType,
    GroupPotentialMemberStatus,
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
    'GroupMemberLeaveResult',
    'GroupBan',
    'GroupMemberApplication',
    'GroupMembership',
    'GetGroupsForMemberResponse',
    'GroupMembershipSearchResponse',
    'GroupApplicationResponse',
    'GroupQuery',
    'GroupNameSearchRequest',
    'GroupEditAction',
    'GroupOptionsEditAction',
    'GroupOptionalConversationAddRequest',
    'GroupOptionalConversationEditRequest',
    'GroupBanRequest',
    'GroupApplicationRequest',
    'GroupApplicationListRequest',
    'GroupPotentialMembership',
    'GroupPotentialMembershipSearchResponse',
]


UserInfoCard = ForwardRef('User.UserInfoCard')
UserMembership = ForwardRef('User.UserMembership')


class GroupUserInfoCard(BaseModel):
    LastSeenDisplayName: str
    LastSeenDisplayNameType: BungieMembershipType
    supplementalDisplayName: Optional[str]
    iconPath: Optional[str]
    crossSaveOverride: BungieMembershipType
    applicableMembershipTypes: List[BungieMembershipType]
    isPublic: bool
    membershipType: BungieMembershipType
    membershipId: int
    displayName: str
    bungieGlobalDisplayName: Optional[str]
    bungieGlobalDisplayNameCode: Optional[str]


class GroupFeatures(BaseModel):
    maximumMembers: int
    maximumMembershipsOfGroupType: int
    capabilities: Capabilities
    membershipTypes: List[BungieMembershipType]
    invitePermissionOverride: bool
    updateCulturePermissionOverride: bool
    hostGuidedGamePermissionOverride: HostGuidedGamesPermissionLevel
    updateBannerPermissionOverride: bool
    joinLevel: RuntimeGroupMemberType


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
    chatSecurity: ChatSecuritySetting
    locale: str
    avatarImageIndex: int
    homepage: GroupHomepage
    membershipOption: MembershipOption
    defaultPublicity: GroupPostPublicity
    theme: str
    bannerPath: str
    avatarPath: str
    conversationId: int
    enableInvitationMessagingForAdmins: bool
    banExpireDate: Optional[ValidatedDatetime]
    features: GroupFeatures
    clanInfo: GroupV2ClanInfoAndInvestment


class GroupMember(BaseModel):
    memberType: RuntimeGroupMemberType
    isOnline: bool
    lastOnlineStatusChange: int
    groupId: int
    destinyUserInfo: GroupUserInfoCard
    bungieNetUserInfo: Optional[UserInfoCard]
    joinDate: ValidatedDatetime


class GroupPotentialMember(BaseModel):
    potentialStatus: GroupPotentialMemberStatus
    groupId: int
    destinyUserInfo: GroupUserInfoCard
    bungieNetUserInfo: UserInfoCard
    joinDate: ValidatedDatetime


class GroupResponse(BaseModel):
    detail: GroupV2
    founder: GroupMember
    alliedIds: List[int]
    parentGroup: Optional[GroupV2]
    allianceStatus: AllianceStatus
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
    membershipOption: MembershipOption
    capabilities: Capabilities
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


class GroupMemberLeaveResult(BaseModel):
    group: GroupV2
    groupDeleted: bool


class GroupBan(BaseModel):
    groupId: int
    lastModifiedBy: UserInfoCard
    createdBy: UserInfoCard
    dateBanned: ValidatedDatetime
    dateExpires: Optional[ValidatedDatetime]
    comment: Optional[str]
    bungieNetUserInfo: Optional[UserInfoCard]
    destinyUserInfo: Optional[GroupUserInfoCard]


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
    resolution: GroupApplicationResolveState


class GroupQuery(BaseModel):
    name: Optional[str]
    groupType: Optional[GroupType]
    creationDate: Optional[GroupDateRange]
    sortBy: Optional[GroupSortBy]
    groupMemberCountFilter: Optional[GroupMemberCountFilter]
    localeFilter: Optional[str]
    tagText: Optional[str]
    itemsPerPage: Optional[int]
    currentPage: Optional[int]
    requestContinuationToken: Optional[str]


class GroupNameSearchRequest(BaseModel):
    groupName: str
    groupType: GroupType


class GroupEditAction(BaseModel):
    name: Optional[str]
    about: Optional[str]
    motto: Optional[str]
    theme: Optional[str]
    avatarImageIndex: Optional[int]
    tags: Optional[str]
    isPublic: Optional[bool]
    membershipOption: Optional[MembershipOption]
    isPublicTopicAdminOnly: Optional[bool]
    allowChat: Optional[bool]
    chatSecurity: Optional[ChatSecuritySetting]
    callsign: Optional[str]
    locale: Optional[str]
    homepage: Optional[GroupHomepage]
    enableInvitationMessagingForAdmins: Optional[bool]
    defaultPublicity: Optional[GroupPostPublicity]


class GroupOptionsEditAction(BaseModel):
    """
    Attributes
    ----------
        InvitePermissionOverride: Optional[:py:class:`bool`]
            Defines the minimum member level allowed to invite new members to the group.
            If this is set to ``True``, ``Admins`` have the power to invite new members, if ``False``, they do not.
            ``Founders`` and ``Acting Founders`` always have the ability to invite new members.
            Defaults to ``False`` for clans, and ``True`` for groups.
        UpdateCulturePermissionOverride: Optional[:py:class:`bool`]
            Defines the minimum member level allowed to update group culture (clan name, motto, banner, etc.).
            If this is set to ``True``, ``Admins`` have the power to update group culture, if ``False``, they do not.
            ``Founders`` and ``Acting Founders`` always have the ability to invite new members.
            Defaults to ``False`` for clans, and ``True`` for groups.
        HostGuidedGamePermissionOverride: Optional[:class:`HostGuidedGamesPermissionLevel`]
            The minimum member level allowed to host guided games. ``Founders``, ``Acting Founders``, and ``Admins``
            can always host guided games. The default is to ``Member`` for clans, and ``None`` for groups, although
            groups do not use this.
        UpdateBannerPermissionOverride: Optional[:py:class:`bool`]
            The minimum member level allowed to update the clan banner. If this is set to ``True``, ``Admins`` can
            edit the clan banner, if ``False``, they cannot. ``Founders`` and ``Acting Founders`` can always edit the
            clan banner.
        JoinLevel: Optional[:class:`RuntimeGroupMemberType`]
            The level that a member will join at when they accept an invite, application, or joining an open clan.
            Defaults to ``Beginner``.
    """

    InvitePermissionOverride: Optional[bool]
    UpdateCulturePermissionOverride: Optional[bool]
    HostGuidedGamePermissionOverride: Optional[HostGuidedGamesPermissionLevel]
    UpdateBannerPermissionOverride: Optional[bool]
    JoinLevel: Optional[RuntimeGroupMemberType]


class GroupOptionalConversationAddRequest(BaseModel):
    chatName: str
    chatSecurity: ChatSecuritySetting


class GroupOptionalConversationEditRequest(BaseModel):
    chatEnabled: Optional[bool]
    chatName: Optional[str]
    chatSecurity: Optional[ChatSecuritySetting]


class GroupBanRequest(BaseModel):
    comment: Optional[str]
    length: Optional[int]


class GroupApplicationRequest(BaseModel):
    message: Optional[str]


class GroupApplicationListRequest(BaseModel):
    memberships: List[UserMembership]
    message: Optional[str]


class GroupPotentialMembership(BaseModel):
    member: GroupPotentialMember
    group: GroupV2


class GroupPotentialMembershipSearchResponse(BaseModel):
    results: List[GroupPotentialMembership]
    totalResults: int
    hasMore: bool
    query: Queries.PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool


from .. import User
