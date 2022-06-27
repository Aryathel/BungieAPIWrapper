from typing import Union

from arya_api_framework import SyncClient, AsyncClient, SubClient
from arya_api_framework.utils import apiclient, endpoint

from ..decorators import destinyclient, oauth_required
from ..models import responses, queries
from ..models.entities.Applications import ApplicationScopes


@destinyclient
@apiclient
class Tokens(SubClient, name='tokens', relative_path='/Tokens'):
    @oauth_required(ApplicationScopes.PartnerOfferGrant)
    @endpoint(
        path='/Tokens/Partner/ClaimOffer/',
        name='Tokens.ClaimPartnerOffer',
        description='Claim a partner offer as the authenticated user.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_Tokens-ClaimPartnerOffer.html'
            '#operation_post_Tokens-ClaimPartnerOffer'
        ),
        method='POST'
    )
    def claim_partner_offer(
            self,
            partner_offer_id: str,
            bungie_net_membership_id: int,
            transaction_id: str
    ) -> responses.Tokens.ClaimPartnerOffer:
        return self.post(
            '/Partner/ClaimOffer/',
            body=queries.Tokens.PartnerOfferClaimRequest(
                PartnerOfferId=partner_offer_id,
                BungieNetMembershipId=bungie_net_membership_id,
                TransactionId=transaction_id
            ),
            response_format=responses.Tokens.ClaimPartnerOffer
        )

    @oauth_required(ApplicationScopes.PartnerOfferGrant)
    @endpoint(
        path='/Tokens/Partner/ApplyMissingOffers/{partnerApplicationId}/{targetBnetMembershipId}/',
        name='Tokens.ApplyMissingPartnerOffersWithoutClaim',
        description=(
                'Apply a partner offer to the targeted user. This endpoint does not claim a new offer, but any already '
                'claimed offers will be applied to the game if not already.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Tokens-ApplyMissingPartnerOffersWithoutClaim.html'
            '#operation_post_Tokens-ApplyMissingPartnerOffersWithoutClaim'
        ),
        method='POST'
    )
    def apply_missing_partner_offers_without_claim(
            self,
            bnet_membership_id: int,
            partner_application_id: int
    ) -> responses.Tokens.ApplyMissingPartnerOffersWithoutClaim:
        return self.post(
            f'/Partner/ApplyMissingOffers/{partner_application_id}/{bnet_membership_id}/',
            response_format=responses.Tokens.ApplyMissingPartnerOffersWithoutClaim
        )

    @oauth_required(ApplicationScopes.PartnerOfferGrant)
    @endpoint(
        path='/Tokens/Partner/History/{partnerApplicationId}/{targetBnetMembershipIp}/',
        name='Tokens.GetPartnerOfferSkuHistory',
        description=(
                'Returns the partner sku and offer history of the targeted user. Elevated permissions are required to '
                'see users that are not yourself.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Tokens-GetPartnerOfferSkuHistory.html'
            '#operation_get_Tokens-GetPartnerOfferSkuHistory'
        ),
        method='GET'
    )
    def get_partner_offer_sku_history(
            self,
            bnet_membership_id: int,
            partner_application_id: int
    ) -> responses.Tokens.GetPartnerOfferSkuHistory:
        return self.get(
            f'/Partner/History/{partner_application_id}/{bnet_membership_id}/',
            response_format=responses.Tokens.GetPartnerOfferSkuHistory
        )

    @oauth_required(ApplicationScopes.ReadAndApplyTokens)
    @endpoint(
        path='/Tokens/Rewards/GetRewardsForUser/{membershipId}/',
        name='Tokens.GetBungieRewardsForUser',
        description='Returns the Bungie rewards for the targeted user.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Tokens-GetBungieRewardsForUser.html'
            '#operation_get_Tokens-GetBungieRewardsForUser'
        ),
        method='GET'
    )
    def get_bungie_rewards_for_user(self, membership_id: int) -> responses.Tokens.GetBungieRewardsForUser:
        return self.get(
            f'/Rewards/GetRewardsForUser/{membership_id}/',
            response_format=responses.Tokens.GetBungieRewardsForUser
        )

    @endpoint(
        path='/Tokens/Rewards/BungieRewards/',
        name='Tokens.GetBungieRewardsList',
        description='Returns a list of the current Bungie rewards.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Tokens-GetBungieRewardsList.html'
            '#operation_get_Tokens-GetBungieRewardsList'
        ),
        method='GET'
    )
    def get_bungie_rewards_list(self) -> responses.Tokens.GetBungieRewardsList:
        return self.get(
            '/Rewards/BungieRewards/',
            response_format=responses.Tokens.GetBungieRewardsList
        )


def setup(client: Union[SyncClient, AsyncClient]) -> None:
    client.add_subclient(Tokens())
