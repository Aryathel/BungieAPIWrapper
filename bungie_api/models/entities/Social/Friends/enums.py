from ...framework import DocumentedIntEnum, DocumentedIntFlag


__all__ = [
    'PresenceStatus',
    'PresenceOnlineStateFlags',
    'FriendRelationshipState',
    'PlatformFriendType',
]


class PresenceStatus(DocumentedIntEnum):
    OfflineOrUnknown = 0
    Online = 1


class PresenceOnlineStateFlags(DocumentedIntFlag):
    None_ = 0
    Destiny1 = 1
    Destiny2 = 2


class FriendRelationshipState(DocumentedIntEnum):
    Unknown = 0
    Friend = 1
    IncomingRequest = 2
    OutgoingRequest = 3


class PlatformFriendType(DocumentedIntEnum):
    Unknown = 0
    Xbox = 1
    PSN = 2
    Steam = 3
