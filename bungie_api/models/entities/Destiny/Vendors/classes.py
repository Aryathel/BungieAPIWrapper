from typing import List

from arya_api_framework import BaseModel

from .....utils import ValidatedDatetime
from .. import (
    DestinyItemQuantity,
    DestinyVendorItemRefundPolicy,
)


__all__ = [
    'DestinyVendorReceipt'
]


class DestinyVendorReceipt(BaseModel):
    currencyPaid: List[DestinyItemQuantity]
    itemReceived: DestinyItemQuantity
    licenseUnlockHash: int
    purchasedByCharacterId: int
    refundPolicy: DestinyVendorItemRefundPolicy
    sequenceNumber: int
    timeToExpiration: int
    expiresOn: ValidatedDatetime
