from arya_api_framework import BaseModel


__all__ = [
    'PartnerOfferClaimRequest',
]


class PartnerOfferClaimRequest(BaseModel):
    PartnerOfferId: str
    BungieNetMembershipId: int
    TransactionId: str
