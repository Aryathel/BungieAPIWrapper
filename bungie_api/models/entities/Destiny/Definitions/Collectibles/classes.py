from typing import Optional, List

from arya_api_framework import BaseModel

from ...enums import DestinyScope, DestinyPresentationNodeType
from .. import Common, Presentation


__all__ = [
    'DestinyCollectibleAcquisitionBlock',
    'DestinyCollectibleStateBlock',
    'DestinyCollectibleDefinition'
]


class DestinyCollectibleAcquisitionBlock(BaseModel):
    acquireMaterialRequirementHash: Optional[int]
    acquireTimestampUnlockValueHash: Optional[int]


class DestinyCollectibleStateBlock(BaseModel):
    obscuredOverrideItemHash: Optional[int]
    requirements: Presentation.DestinyPresentationNodeRequirementsBlock


class DestinyCollectibleDefinition(BaseModel):
    displayProperties: Common.DestinyDisplayPropertiesDefinition
    scope: DestinyScope
    sourceString: str
    sourceHash: Optional[int]
    itemHash: Optional[int]
    acquisitionInfo: DestinyCollectibleAcquisitionBlock
    stateInfo: DestinyCollectibleStateBlock
    presentationInfo: Presentation.DestinyPresentationChildBlock
    presentationNodeType: DestinyPresentationNodeType
    traitIds: List[str]
    traitHashes: List[int]
    parentNodeHashes: List[int]
    hash: int
    index: int
    redacted: bool
