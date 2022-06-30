from typing import (
    List,
    Mapping,
    Optional,
    Union,
)

from arya_api_framework import BaseModel

from ... import User


__all__ = [
    'CoreSystem',
    'CoreSetting',
    'Destiny2CoreSettings',
    'CoreSettingsConfiguration',
]


class CoreSystem(BaseModel):
    enabled: bool
    parameters: Mapping[str, Union[float, bool, int, str]]


class CoreSetting(BaseModel):
    identifier: str
    isDefault: bool
    displayName: Optional[str]
    summary: Optional[str]
    imagePath: Optional[str]
    childSettings: Optional[List['CoreSetting']]


class Destiny2CoreSettings(BaseModel):
    collectionRootNode: int
    badgesRootNode: int
    recordsRootNode: int
    medalsRootNode: int
    metricsRootNode: int
    activeTriumphsRootNodeHash: int
    activeSealsRootNodeHash: int
    legacyTriumphsRootNodeHash: int
    legacySealsRootNodeHash: int
    medalsRootNodeHash: int
    exoticCatalystsRootNodeHash: int
    loreRootNodeHash: int
    craftingRootNodeHash: int
    currentRankProgressionHashes: List[int]
    insertPlugFreeProtectedPlugItemHashes: List[int]
    insertPlugFreeBlockedSocketTypeHashes: List[int]
    undiscoveredCollectibleImage: str
    ammoTypeHeavyIcon: str
    ammoTypeSpecialIcon: str
    ammoTypePrimaryIcon: str
    currentSeasonalArtifactHash: int
    currentSeasonHash: int
    seasonalChallengesPresentationNodeHash: int
    futureSeasonHashes: List[int]
    pastSeasonHashes: List[int]


class CoreSettingsConfiguration(BaseModel):
    environment: str
    systems: Mapping[str, CoreSystem]
    ignoreReasons: List[CoreSetting]
    forumCategories: List[CoreSetting]
    groupAvatars: List[CoreSetting]
    destinyMembershipTypes: List[CoreSetting]
    recruitmentPlatformTags: List[CoreSetting]
    recruitmentMiscTags: List[CoreSetting]
    recruitmentActivities: List[CoreSetting]
    userContentLocales: List[CoreSetting]
    systemContentLocales: List[CoreSetting]
    clanBannerDecals: List[CoreSetting]
    clanBannerDecalColors: List[CoreSetting]
    clanBannerGonfalons: List[CoreSetting]
    clanBannerGonfalonColors: List[CoreSetting]
    clanBannerGonfalonDetails: List[CoreSetting]
    clanBannerGonfalonDetailColors: List[CoreSetting]
    clanBannerStandards: List[CoreSetting]
    destiny2CoreSettings: Destiny2CoreSettings
    emailSettings: User.EmailSettings
    fireteamActivities: List[CoreSetting]
