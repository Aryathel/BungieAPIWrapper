from typing import (
    Mapping,
    List,
    Optional
)

from .framework import BaseResponse, PaginatedBaseResponse
from .. import entities


__all__ = [
    'GetCurrentBungieNetUser',
    'GetBungieNetUserById',
    'GetSanitizedPlatformDisplayNames',
    'GetCredentialTypesForTargetAccount',
    'GetAvailableThemes',
    'GetMembershipDataById',
    'GetMembershipDataForCurrentUser',
]


class GetCurrentBungieNetUser(BaseResponse):
    Response: entities.User.GeneralUser


class GetBungieNetUserById(BaseResponse):
    Response: entities.User.GeneralUser


class GetSanitizedPlatformDisplayNames(BaseResponse):
    Response: Mapping[str, str]


class GetCredentialTypesForTargetAccount(BaseResponse):
    Response: List[entities.User.Models.GetCredentialTypesForAccountResponse]


class GetAvailableThemes(BaseResponse):
    Response: List[entities.Config.UserTheme]


class GetMembershipDataById(BaseResponse):
    Response: entities.User.UserMembershipData


class GetMembershipDataForCurrentUser(BaseResponse):
    Response: entities.User.UserMembershipData


class GetMembershipFromHardLinkedCredential(BaseResponse):
    Response: entities.User.HardLinkedUserMembership


class SearchByGlobalNamePost(PaginatedBaseResponse):
    Response: entities.User.UserSearchResponse

    @property
    def is_paginating(self) -> bool:
        return self.Response.hasMore

    @property
    def next(self) -> Optional[int]:
        if self.is_paginating:
            return self.Response.page+1

    @property
    def start(self) -> None:
        return

    @property
    def end(self) -> None:
        return

    @property
    def previous(self) -> None:
        return
