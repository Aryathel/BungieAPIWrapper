from ...framework import DocumentedIntEnum


__all__ = [
    'BungieCredentialType',
]


class BungieCredentialType(DocumentedIntEnum):
    None_ = 0
    Xuid = 1
    Psnid = 2
    Wlid = 3
    Fake = 4
    Facebook = 5
    Google = 8
    Windows = 9
    DemonId = 10
    SteamId = 12
    BattleNetId = 14
    StadiaId = 16
    TwitchId = 18
