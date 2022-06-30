from ..framework import DocumentedIntEnum


__all__ = [
    'FireteamDateRange',
    'FireteamPlatform',
    'FireteamPublicSearchOption',
    'FireteamSlotSearch',
    'FireteamPlatformInviteResult',
]


class FireteamDateRange(DocumentedIntEnum):
    All = 0
    Now = 1
    TwentyFourHours = 2
    FortyEightHours = 3
    ThisWeek = 4


class FireteamPlatform(DocumentedIntEnum):
    Any = 0
    Playstation4 = 1
    XboxOne = 2
    Blizzard = 3
    Steam = 4
    Stadia = 5


class FireteamPublicSearchOption(DocumentedIntEnum):
    PublicAndPrivate = 0
    PublicOnly = 1
    PrivateOnly = 2


class FireteamSlotSearch(DocumentedIntEnum):
    NoSlotRestrictions = 0
    HasOpenPlayerSlots = 1
    HasOpenPlayerOrAltSlots = 2


class FireteamPlatformInviteResult(DocumentedIntEnum):
    None_ = 0
    Success = 1
    AlreadyInFireteam = 2
    Throttled = 3
    ServiceError = 4
