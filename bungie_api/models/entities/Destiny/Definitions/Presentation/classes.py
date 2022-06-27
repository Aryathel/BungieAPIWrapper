from typing import List

from arya_api_framework import BaseModel

from ...enums import DestinyPresentationNodeType, DestinyPresentationDisplayStyle


__all__ = [
    'DestinyPresentationNodeRequirementsBlock',
    'DestinyPresentationChildBlock',
]


class DestinyPresentationNodeRequirementsBlock(BaseModel):
    entitlementUnavailableMessage: str


class DestinyPresentationChildBlock(BaseModel):
    presentationNodeType: DestinyPresentationNodeType
    parentPresentationNodeHashes: List[int]
    displayStyle: DestinyPresentationDisplayStyle
