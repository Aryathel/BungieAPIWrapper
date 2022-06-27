from typing import (
    List,
    Optional,
)

from arya_api_framework import BaseModel


__all__ = [
    'DestinyIconSequenceDefinition',
    'DestinyDisplayPropertiesDefinition'
]


class DestinyIconSequenceDefinition(BaseModel):
    frames: List[str]


class DestinyDisplayPropertiesDefinition(BaseModel):
    description: str
    name: str
    icon: str
    iconSequences: Optional[List[DestinyIconSequenceDefinition]]
    highResIcon: Optional[str]
    hasIcon: bool
