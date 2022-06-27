from typing import (
    List,
    Optional,
    Union,
)

from arya_api_framework import BaseModel

from ....utils import ValidatedDatetime
from ..enums import BungieMembershipType
from .. import Destiny


__all__ = [
    'PartnerOfferHistoryResponse',
    'PartnerOfferSkuHistoryResponse',
]


class PartnerOfferHistoryResponse(BaseModel):
    PartnerOfferKey: str
    MembershipId: Optional[int]
    MembershipType: Optional[BungieMembershipType]
    LocalizedName: str
    LocalizedDescription: str
    IsConsumable: bool
    QuantityApplied: int
    ApplyDate: Optional[ValidatedDatetime]


class PartnerOfferSkuHistoryResponse(BaseModel):
    SkuIdentifier: str
    LocalizedName: str
    LocalizedDescription: str
    ClaimDate: ValidatedDatetime
    AllOffersApplied: bool
    TransactionId: str
    SkuOffers: List[PartnerOfferHistoryResponse]


class CollectibleDefinitions(BaseModel):
    CollectibleDefinition: Destiny.Definitions.Collectibles.DestinyCollectibleDefinition
    DestinyInventoryItemDefinition: Destiny.Definitions.DestinyInventoryItemDefinition


class RewardAvailabilityModel(BaseModel):
    HasExistingCode: bool
    RecordDefinitions: List[Destiny.Definitions.Records.DestinyRecordDefinition]
    CollectibleDefinitions: List[CollectibleDefinitions]
    IsOffer: bool
    HasOffer: bool
    OfferApplied: bool
    DecryptedToken: Optional[str]
    IsLoyaltyReward: bool
    ShopifyEndDate: Optional[ValidatedDatetime]
    GameEarnByDate: ValidatedDatetime
    RedemptionEndDate: ValidatedDatetime


class UserRewardAvailabilityModel(BaseModel):
    AvailabilityModel: RewardAvailabilityModel
    IsAvailableForUser: bool
    IsUnlockedForUser: bool


class RewardDisplayProperties(BaseModel):
    Name: str
    Description: str
    ImagePath: str


class BungieRewardDisplay(BaseModel):
    UserRewardAvailabilityModel: UserRewardAvailabilityModel
    ObjectiveDisplayProperties: Optional[RewardDisplayProperties]
    RewardDisplayProperties: RewardDisplayProperties
