from typing import Mapping

from arya_api_framework import BaseModel


__all__ = [
    'DestinyStringVariablesComponent',
]


class DestinyStringVariablesComponent(BaseModel):
    integerValuesByHash: Mapping[int, int]
