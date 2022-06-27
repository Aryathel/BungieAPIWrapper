from typing import List, Mapping

from arya_api_framework import BaseModel


__all__ = [
    'GearAssetDataBaseDefinition',
    'ImagePyramidEntry',
    'DestinyManifest',
]


class GearAssetDataBaseDefinition(BaseModel):
    version: int
    path: str


class ImagePyramidEntry(BaseModel):
    name: str
    factor: float


class DestinyManifest(BaseModel):
    version: str
    mobileAssetContentPath: str
    mobileGearAssetDataBases: List[GearAssetDataBaseDefinition]
    mobileWorldContentPaths: Mapping[str, str]
    jsonWorldContentPaths: Mapping[str, str]
    jsonWorldComponentContentPaths: Mapping[str, Mapping[str, str]]
    mobileClanBannerDatabasePath: str
    mobileGearCDN: Mapping[str, str]
    iconImagePyramidInfo: List[ImagePyramidEntry]
