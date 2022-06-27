from typing import (
    List,
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel


__all__ = [
    'DestinyCraftableComponent',
    'DestinyCraftablesComponent',
    'DestinyCraftableSocketComponent',
    'DestinyCraftableSocketPlugComponent',
]


class DestinyCraftableSocketPlugComponent(BaseModel):
    plugItemHash: int
    failedRequirementIndexes: List[int]


class DestinyCraftableSocketComponent(BaseModel):
    plugSetHash: int
    plugs: Optional[List[DestinyCraftableSocketPlugComponent]]


class DestinyCraftableComponent(BaseModel):
    visible: bool
    failedRequirementIndexes: List[int]
    sockets: List[DestinyCraftableSocketComponent]


class DestinyCraftablesComponent(BaseModel):
    craftables: Mapping[int, DestinyCraftableComponent]
    craftingRootNodeHash: int
