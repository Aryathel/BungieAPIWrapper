from ..framework import DocumentedIntEnum


__all__ = [
    'GroupType',
    'GroupMemberCountFilter',
    'GroupSortBy',
    'GroupDateRange',
    'HostGuidedGamesPermissionLevel',
    'ChatSecuritySetting',
    'MembershipOption',
    'GroupHomepage',
    'GroupPostPublicity',
    'RuntimeGroupMemberType',
    'GroupApplicationResolveState',
    'GroupsForMemberFilter',
]


class GroupType(DocumentedIntEnum):
    General = 0
    Clan = 1


class GroupMemberCountFilter(DocumentedIntEnum):
    All = 0
    OneToTen = 1
    ElevenToOneHundred = 2
    GreaterThanOneHundred = 3


class GroupSortBy(DocumentedIntEnum):
    Name = 0
    Date = 1
    Popularity = 2
    Id = 3


class GroupDateRange(DocumentedIntEnum):
    All = 0
    PastDay = 1
    PastWeek = 2
    PastMonth = 3
    PastYear = 4


class HostGuidedGamesPermissionLevel(DocumentedIntEnum):
    None_ = 0
    Beginner = 1
    Member = 2


class ChatSecuritySetting(DocumentedIntEnum):
    Group = 0
    Admins = 1


class MembershipOption(DocumentedIntEnum):
    Reviewed = 0
    Open = 1
    Closed = 2


class GroupHomepage(DocumentedIntEnum):
    Wall = 0
    Forum = 1
    AllianceForum = 2


class GroupPostPublicity(DocumentedIntEnum):
    Public = 0
    Alliance = 1
    Private = 2


class RuntimeGroupMemberType(DocumentedIntEnum):
    None_ = 0
    Beginner = 1
    Member = 2
    Admin = 3
    ActingFounder = 4
    Founder = 5


class GroupApplicationResolveState(DocumentedIntEnum):
    Unresolved = 0
    Accepted = 1
    Denied = 2
    Rescinded = 3


class GroupsForMemberFilter(DocumentedIntEnum):
    All = 0
    Founded = 1
    NonFounded = 2
