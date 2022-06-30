from typing import (
    List,
    Optional,
)

from arya_api_framework import BaseModel

from ......utils import ValidatedDatetime
from ... import (
    DestinyProgression,
    DestinyItemQuantity,
    DestinyUnlockStatus,
    VendorItemStatus,
)


__all__ = [
    'DestinyVendorComponent',
    'DestinyVendorCategory',
    'DestinyVendorCategoriesComponent',
    'DestinyVendorSaleItemComponent',
]


class DestinyVendorComponent(BaseModel):
    canPurchase: bool
    progression: Optional[DestinyProgression]
    vendorLocationIndex: int
    seasonalRank: Optional[int]
    vendorHash: int
    nextRefreshDate: ValidatedDatetime
    enabled: bool


class DestinyVendorCategory(BaseModel):
    displayCategoryIndex: int
    itemIndexes: List[int]


class DestinyVendorCategoriesComponent(BaseModel):
    categories: List[DestinyVendorCategory]


class DestinyVendorSaleItemComponent(BaseModel):
    saleStatus: VendorItemStatus
    requiredUnlocks: Optional[List[int]]
    unlockStatuses: Optional[List[DestinyUnlockStatus]]
    failureIndexes: List[int]
    augments: int
    itemValueVisibility: Optional[List[bool]]
    vendorItemIndex: int
    itemHash: int
    overrideStyleItemHash: Optional[int]
    quantity: int
    costs: List[DestinyItemQuantity]
    overrideNextRefreshDate: Optional[ValidatedDatetime]
    apiPurchasable: Optional[bool]
