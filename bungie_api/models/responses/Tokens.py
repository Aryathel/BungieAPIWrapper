from typing import List, Mapping

from .. import entities
from .framework import BaseResponse


__all__ = [
    'ClaimPartnerOffer',
    'ApplyMissingPartnerOffersWithoutClaim',
]


class ClaimPartnerOffer(BaseResponse):
    Response: bool


class ApplyMissingPartnerOffersWithoutClaim(BaseResponse):
    Response: bool


class GetPartnerOfferSkuHistory(BaseResponse):
    Response: List[entities.Tokens.PartnerOfferSkuHistoryResponse]


class GetBungieRewardsForUser(BaseResponse):
    Response: Mapping[str, entities.Tokens.BungieRewardDisplay]


class GetBungieRewardsList(BaseResponse):
    Response: Mapping[str, entities.Tokens.BungieRewardDisplay]
