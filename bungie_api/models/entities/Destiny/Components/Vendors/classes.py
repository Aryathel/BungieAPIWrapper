from typing import (
    List,
    Optional,
)

from arya_api_framework import BaseModel

from ......utils import ValidatedDatetime
from ... import DestinyItemQuantity


__all__ = [
    'DestinyVendorGroup',
    'DestinyVendorGroupComponent',
    'DestinyPublicVendorComponent',
    'DestinyPublicVendorSaleItemComponent',
]


class DestinyVendorGroup(BaseModel):
    vendorGroupHash: int
    vendorHashes: List[int]


class DestinyVendorGroupComponent(BaseModel):
    groups: List[DestinyVendorGroup]


class DestinyPublicVendorComponent(BaseModel):
    vendorHash: int
    nextRefreshDate: ValidatedDatetime
    enabled: bool


class DestinyPublicVendorSaleItemComponent(BaseModel):
    vendorItemIndex: int
    itemHash: int
    overrideStyleItemHash: Optional[int]
    quantity: int
    costs: List[DestinyItemQuantity]
    overrideNextRefreshDate: Optional[ValidatedDatetime]
    apiPurchasable: Optional[bool]
