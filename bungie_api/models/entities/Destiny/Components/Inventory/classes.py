from typing import (
    ForwardRef,
    Mapping,
)

from arya_api_framework import BaseModel

from .....entities.enums import BungieMembershipType
from ... import Entities


__all__ = [
    'DestinyPlatformSilverComponent',
    'DestinyCurrenciesComponent',
]


class DestinyPlatformSilverComponent(BaseModel):
    platformSilver: Mapping[BungieMembershipType, Entities.Items.DestinyItemComponent]


class DestinyCurrenciesComponent(BaseModel):
    itemQuantities: Mapping[int, int]
