from .framework import DocumentedIntEnum


__all__ = [
    'BungieMembershipType',
]


class BungieMembershipType(DocumentedIntEnum):
    None_ = 0
    TigerXbox = 1
    TigerPsn = 2
    TigerSteam = 3
    TigerBlizzard = 4
    TigerStadia = 5
    TigerDemon = 10
    BungieNext = 254
    All = -1, (
        '"All" is only valid for searching capabilities: you need to pass the actual matching BungieMembershipType for '
        'any query where you pass a known membershipId.'
    )
