from typing import (
    ForwardRef,
    List,
    Optional,
)

from arya_api_framework import BaseModel

from ......utils import ValidatedDatetime
from ... import (
    DestinyGameVersions,
    Vendors,
)


UserInfoCard = ForwardRef('User.UserInfoCard')


__all__ = [
    'DestinyVendorReceiptsComponent',
    'DestinyProfileComponent',
]


class DestinyVendorReceiptsComponent(BaseModel):
    receipts: List[Vendors.DestinyVendorReceipt]


class DestinyProfileComponent(BaseModel):
    userInfo: UserInfoCard
    dateLastPlayed: ValidatedDatetime
    versionsOwned: DestinyGameVersions
    characterIds: List[int]
    seasonHashes: List[int]
    currentSeasonHash: Optional[int]
    currentSeasonRewardPowerCap: Optional[int]


from .... import User
