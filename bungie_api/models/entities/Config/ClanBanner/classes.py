from typing import (
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel

from ... import Destiny


__all__ = [
    'ClanBannerDecal',
    'ClanBannerSource',
]


class ClanBannerDecal(BaseModel):
    identifier: Optional[str]
    foregroundPath: str
    backgroundPath: str


class ClanBannerSource(BaseModel):
    clanBannerDecals: Mapping[int, ClanBannerDecal]
    clanBannerDecalPrimaryColors: Mapping[int, Destiny.Misc.DestinyColor]
    clanBannerDecalSecondaryColors: Mapping[int, Destiny.Misc.DestinyColor]
    clanBannerGonfalons: Mapping[int, str]
    clanBannerGonfalonColors: Mapping[int, Destiny.Misc.DestinyColor]
    clanBannerGonfalonDetails: Mapping[int, str]
    clanBannerGonfalonDetailColors: Mapping[int, Destiny.Misc.DestinyColor]
    clanBannerDecalsSquare: Mapping[int, ClanBannerDecal]
    clanBannerGonfalonDetailsSquare: Mapping[int, str]
