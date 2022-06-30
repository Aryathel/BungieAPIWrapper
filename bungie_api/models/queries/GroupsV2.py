from typing import Optional

from arya_api_framework import BaseModel

from .. import entities


__all__ = [
    'GetMembersOfGroup',
    'GetAdminsAndFounderOfGroup',
    'GetBannedMembersOfGroup',
    'GetPendingMemberships',
    'GetInvitedIndividuals',
]


class GetMembersOfGroup(BaseModel):
    currentpage: Optional[int]
    memberType: Optional[entities.GroupsV2.RuntimeGroupMemberType]
    nameSearch: Optional[str]


class GetAdminsAndFounderOfGroup(BaseModel):
    currentpage: Optional[int]


class GetBannedMembersOfGroup(BaseModel):
    currentpage: Optional[int]


class GetPendingMemberships(BaseModel):
    currentpage: Optional[int]


class GetInvitedIndividuals(BaseModel):
    currentpage: Optional[int]
