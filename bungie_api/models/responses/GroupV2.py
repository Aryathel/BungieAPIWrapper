from typing import Dict, List, Optional

from .. import entities
from .framework import BaseResponse, PaginatedBaseResponse


__all__ = [
    'GetAvailableAvatars',
    'GetAvailableThemes',
    'GetUserClanInviteSetting',
    'GetRecommendedGroups',
    'GroupSearch',
    'GetGroup',
    'GetGroupByName',
    'GetGroupByNameV2',
    'GetGroupOptionalConversations',
    'EditGroup',
    'EditClanBanner',
    'EditFounderOptions',
    'AddOptionalConversation',
    'EditOptionalConversation',
    'GetMembersOfGroup',
    'GetAdminsAndFounderOfGroup',
    'EditGroupMembership',
    'KickMember',
    'BanMember',
    'UnbanMember',
    'GetBannedMembersOfGroup',
    'AbdicateFoundership',
    'GetPendingMemberships',
    'GetInvitedIndividuals',
    'ApproveAllPending',
    'DenyAllPending',
    'ApprovePendingForList',
    'ApprovePending',
    'DenyPendingForList',
    'GetGroupsForMember',
    'RecoverGroupForFounder',
    'GetPotentialGroupsForMember',
    'IndividualGroupInvite',
    'IndividualGroupInviteCancel',
]


class GetAvailableAvatars(BaseResponse):
    Response: Dict[int, str]


class GetAvailableThemes(BaseResponse):
    Response: List[entities.Config.GroupTheme]


class GetUserClanInviteSetting(BaseResponse):
    Response: bool


class GetRecommendedGroups(BaseResponse):
    Response: List[entities.GroupsV2.GroupV2Card]


class GroupSearch(PaginatedBaseResponse):
    Response: entities.GroupsV2.GroupSearchResponse

    @property
    def is_paginating(self) -> bool:
        return self.Response.hasMore

    @property
    def next(self) -> Optional[int]:
        if self.is_paginating:
            return self.Response.query.currentPage + 1

    @property
    def previous(self) -> None:
        return

    @property
    def end(self) -> None:
        return

    @property
    def start(self) -> None:
        return


class GetGroup(BaseResponse):
    Response: entities.GroupsV2.GroupResponse


class GetGroupByName(BaseResponse):
    Response: entities.GroupsV2.GroupResponse


class GetGroupByNameV2(BaseResponse):
    Response: entities.GroupsV2.GroupResponse


class GetGroupOptionalConversations(BaseResponse):
    Response: List[entities.GroupsV2.GroupOptionalConversation]


class EditGroup(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class EditClanBanner(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class EditFounderOptions(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class AddOptionalConversation(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class EditOptionalConversation(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class GetMembersOfGroup(PaginatedBaseResponse):
    Response: entities.SearchResultOfGroupMember

    @property
    def is_paginating(self) -> bool:
        return self.Response.hasMore

    @property
    def next(self) -> Optional[int]:
        if self.is_paginating:
            return self.Response.query.currentPage + 1

    @property
    def previous(self) -> None:
        return

    @property
    def start(self) -> None:
        return

    @property
    def end(self) -> None:
        return


class GetAdminsAndFounderOfGroup(PaginatedBaseResponse):
    Response: entities.SearchResultOfGroupMember

    @property
    def is_paginating(self) -> bool:
        return self.Response.hasMore

    @property
    def next(self) -> Optional[int]:
        if self.is_paginating:
            return self.Response.query.currentPage + 1

    @property
    def previous(self) -> None:
        return

    @property
    def start(self) -> None:
        return

    @property
    def end(self) -> None:
        return


class EditGroupMembership(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class KickMember(BaseResponse):
    Response: entities.GroupsV2.GroupMemberLeaveResult


class BanMember(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class UnbanMember(BaseResponse):
    Response: entities.Exceptions.PlatformErrorCodes


class GetBannedMembersOfGroup(PaginatedBaseResponse):
    Response: entities.SearchResultOfGroupBan

    @property
    def is_paginating(self) -> bool:
        return self.Response.hasMore

    @property
    def next(self) -> Optional[int]:
        if self.is_paginating:
            return self.Response.query.currentPage + 1

    @property
    def previous(self) -> None:
        return

    @property
    def start(self) -> None:
        return

    @property
    def end(self) -> None:
        return


class AbdicateFoundership(BaseResponse):
    Response: bool


class GetPendingMemberships(PaginatedBaseResponse):
    Response: entities.SearchResultOfGroupMemberApplication

    @property
    def is_paginating(self) -> bool:
        return self.Response.hasMore

    @property
    def next(self) -> Optional[int]:
        if self.is_paginating:
            return self.Response.query.currentPage + 1

    @property
    def previous(self) -> None:
        return

    @property
    def start(self) -> None:
        return

    @property
    def end(self) -> None:
        return


class GetInvitedIndividuals(PaginatedBaseResponse):
    Response: entities.SearchResultOfGroupMemberApplication

    @property
    def is_paginating(self) -> bool:
        return self.Response.hasMore

    @property
    def next(self) -> Optional[int]:
        if self.is_paginating:
            return self.Response.query.currentPage + 1

    @property
    def previous(self) -> None:
        return

    @property
    def start(self) -> None:
        return

    @property
    def end(self) -> None:
        return


class ApproveAllPending(BaseResponse):
    Response: List[entities.Entities.EntityActionResult]


class DenyAllPending(BaseResponse):
    Response: List[entities.Entities.EntityActionResult]


class ApprovePendingForList(BaseResponse):
    Response: List[entities.Entities.EntityActionResult]


class ApprovePending(BaseResponse):
    Response: bool


class DenyPendingForList(BaseResponse):
    Response: List[entities.Entities.EntityActionResult]


class GetGroupsForMember(PaginatedBaseResponse):
    Response: entities.GroupsV2.GetGroupsForMemberResponse

    @property
    def is_paginating(self) -> bool:
        return self.Response.hasMore

    @property
    def next(self) -> Optional[int]:
        if self.is_paginating:
            return self.Response.query.currentPage + 1

    @property
    def previous(self) -> None:
        return

    @property
    def start(self) -> None:
        return

    @property
    def end(self) -> None:
        return


class RecoverGroupForFounder(PaginatedBaseResponse):
    Response: entities.GroupsV2.GroupMembershipSearchResponse

    @property
    def is_paginating(self) -> bool:
        return self.Response.hasMore

    @property
    def next(self) -> Optional[int]:
        if self.is_paginating:
            return self.Response.query.currentPage + 1

    @property
    def previous(self) -> None:
        return

    @property
    def start(self) -> None:
        return

    @property
    def end(self) -> None:
        return


class GetPotentialGroupsForMember(PaginatedBaseResponse):
    Response: entities.GroupsV2.GroupPotentialMembershipSearchResponse

    @property
    def is_paginating(self) -> bool:
        return self.Response.hasMore

    @property
    def next(self) -> Optional[int]:
        if self.is_paginating:
            return self.Response.query.currentPage + 1

    @property
    def previous(self) -> None:
        return

    @property
    def start(self) -> None:
        return

    @property
    def end(self) -> None:
        return


class IndividualGroupInvite(BaseResponse):
    Response: entities.GroupsV2.GroupApplicationResponse


class IndividualGroupInviteCancel(BaseResponse):
    Response: entities.GroupsV2.GroupApplicationResponse
