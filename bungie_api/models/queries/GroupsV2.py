from typing import Optional, List

from arya_api_framework import BaseModel

from .. import entities


__all__ = [
    'GroupQuery',
    'GroupNameSearchRequest',
    'GroupEditAction',
    'GroupOptionsEditAction',
    'GroupOptionalConversationAddRequest',
    'GroupOptionalConversationEditRequest',
    'GetMembersOfGroup',
    'GetAdminsAndFounderOfGroup',
    'GroupBanRequest',
    'GetBannedMembersOfGroup',
    'GetPendingMemberships',
    'GetInvitedIndividuals',
    'GroupApplicationRequest',
    'GroupApplicationListRequest',
]


class GroupQuery(BaseModel):
    name: Optional[str]
    groupType: Optional[entities.GroupsV2.GroupType]
    creationDate: Optional[entities.GroupsV2.GroupDateRange]
    sortBy: Optional[entities.GroupsV2.GroupSortBy]
    groupMemberCountFilter: Optional[entities.GroupsV2.GroupMemberCountFilter]
    localeFilter: Optional[str]
    tagText: Optional[str]
    itemsPerPage: Optional[int]
    currentPage: Optional[int]
    requestContinuationToken: Optional[str]


class GroupNameSearchRequest(BaseModel):
    groupName: str
    groupType: entities.GroupsV2.GroupType


class GroupEditAction(BaseModel):
    name: Optional[str]
    about: Optional[str]
    motto: Optional[str]
    theme: Optional[str]
    avatarImageIndex: Optional[int]
    tags: Optional[str]
    isPublic: Optional[bool]
    membershipOption: Optional[entities.GroupsV2.MembershipOption]
    isPublicTopicAdminOnly: Optional[bool]
    allowChat: Optional[bool]
    chatSecurity: Optional[entities.GroupsV2.ChatSecuritySetting]
    callsign: Optional[str]
    locale: Optional[str]
    homepage: Optional[entities.GroupsV2.GroupHomepage]
    enableInvitationMessagingForAdmins: Optional[bool]
    defaultPublicity: Optional[entities.GroupsV2.GroupPostPublicity]


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
    UpdateCulturePermissionoverride: Optional[bool]
    HostGuidedGamePermissionOverride: Optional[entities.GroupsV2.HostGuidedGamesPermissionLevel]
    UpdateBannerPermissionOverride: Optional[bool]
    JoinLevel: Optional[entities.GroupsV2.RuntimeGroupMemberType]


class GroupOptionalConversationAddRequest(BaseModel):
    chatName: str
    chatSecurity: entities.GroupsV2.ChatSecuritySetting


class GroupOptionalConversationEditRequest(BaseModel):
    chatEnabled: Optional[bool]
    chatName: Optional[str]
    chatSecurity: Optional[entities.GroupsV2.ChatSecuritySetting]


class GetMembersOfGroup(BaseModel):
    currentpage: Optional[int]
    memberType: Optional[entities.GroupsV2.RuntimeGroupMemberType]
    nameSearch: Optional[str]


class GetAdminsAndFounderOfGroup(BaseModel):
    currentpage: Optional[int]


class GroupBanRequest(BaseModel):
    comment: Optional[str]
    length: Optional[int]


class GetBannedMembersOfGroup(BaseModel):
    currentpage: Optional[int]


class GetPendingMemberships(BaseModel):
    currentpage: Optional[int]


class GetInvitedIndividuals(BaseModel):
    currentpage: Optional[int]


class GroupApplicationRequest(BaseModel):
    message: Optional[str]


class GroupApplicationListRequest(BaseModel):
    memberships: List[entities.User.UserMembership]
    message: Optional[str]
