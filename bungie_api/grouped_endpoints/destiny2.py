from typing import (
    List,
    Optional,
    Union,
)

from arya_api_framework import SyncClient, AsyncClient, SubClient
from arya_api_framework.utils import apiclient, endpoint

# from ..decorators import destinyclient, oauth_required
from ..models import responses, queries
from ..models.entities import (
    BungieMembershipType,
    Destiny,
)


MemberType = Union[int, BungieMembershipType]
ComponentType = Union[int, str, Destiny.DestinyComponentType]


@apiclient
class Destiny2(SubClient, name='destiny2', relative_path='/Destiny2'):
    @endpoint(
        path='/Destiny2/Manifest/',
        name='Destiny2.GetDestinyManifest',
        description='Returns the current version of the manifest as a JSON object.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetDestinyManifest.html'
            '#operation_get_Destiny2-GetDestinyManifest'
        ),
        method='GET'
    )
    def get_destiny_manifest(self) -> responses.Destiny2.GetDestinyManifest:
        return self.get(
            '/Manifest/',
            response_format=responses.Destiny2.GetDestinyManifest
        )

    @endpoint(
        path='/Destiny2/Manifest/{entityType}/{hashIdentifier}/',
        name='Destiny2.GetDestinyEntityDefinition',
        description=(
            'Returns the static definition of an entity of the given Type and hash identifier. Examine the API '
            'Documentation for the Type Names of entities that have their own definitions. Note that the return '
            'type will always *inherit from* DestinyDefinition, but the specific type returned will be the requested '
            'entity type if it can be found. Please don\'t use this as a chatty alternative to the Manifest database '
            'if you require large sets of data, but for simple and one-off accesses this should be handy.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetDestinyEntityDefinition.html'
            '#operation_get_Destiny2-GetDestinyEntityDefinition'
        ),
        method='GET'
    )
    def get_destiny_entity_definition(
            self,
            entity_type: str,
            hash_identifier: int
    ) -> responses.Destiny2.GetDestinyEntityDefinition:
        return self.get(
            f'/Manifest/{entity_type}/{hash_identifier}/',
            response_format=responses.Destiny2.GetDestinyEntityDefinition
        )

    @endpoint(
        path='/Destiny2/SearchDestinyPlayerByBungieName/{membershipType}/',
        name='Destiny2.SearchDestinyPlayerByBungieName',
        description=(
            'Returns a list of Destiny memberships given a global Bungie Display Name. This method will hide '
            'overridden memberships due to cross save.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Destiny2-SearchDestinyPlayerByBungieName.html'
            '#operation_post_Destiny2-SearchDestinyPlayerByBungieName'
        ),
        method='POST'
    )
    def search_destiny_player_by_bungie_name(
            self,
            display_name: str,
            display_name_code: int,
            membership_type: MemberType
    ) -> responses.Destiny2.SearchDestinyPlayerByBungieName:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.post(
            f'/SearchDestinyPlayerByBungieName/{membership_type}',
            body=queries.User.ExactSearchRequest(
                displayName=display_name,
                displayNameCode=display_name_code
            ),
            response_format=responses.Destiny2.SearchDestinyPlayerByBungieName
        )

    @endpoint(
        path='/Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/',
        name='Destiny2.GetLinkedProfiles',
        description=(
            'Returns a summary information about all profiles linked to the requesting membership type/membership ID '
            'that have valid Destiny information. The passed-in Membership Type/Membership ID may be a Bungie.Net '
            'membership or a Destiny membership. It only returns the minimal amount of data to begin making more '
            'substantive requests, but will hopefully serve as a useful alternative to UserServices for people who '
            'just care about Destiny data. Note that it will only return linked accounts whose linkages you are '
            'allowed to view.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetLinkedProfiles.html'
            '#operation_get_Destiny2-GetLinkedProfiles'
        ),
        method='GET'
    )
    def get_linked_profiles(
            self,
            membership_id: int,
            membership_type: MemberType,
            get_all_memberships: Optional[bool] = None
    ) -> responses.Destiny2.GetLinkedProfiles:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.get(
            f'/{membership_type}/Profile/{membership_id}/LinkedProfiles/',
            parameters=queries.Destiny2.GetLinkedProfiles(getAllMemberships=get_all_memberships),
            response_format=responses.Destiny2.GetLinkedProfiles
        )

    @endpoint(
        path='/Destiny2/{membershipType}/Profile/{destinyMembershipId}/',
        name='Destiny2.GetProfile',
        description='Returns the destiny profile information for the supplied membership.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetProfile.html'
            '#operation_get_Destiny2-GetProfile'
        ),
        method='GET'
    )
    def get_profile(
            self,
            membership_id: int,
            membership_type: MemberType,
            components: Union[ComponentType, List[ComponentType]]
    ) -> responses.Destiny2.GetProfile:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.get(
            f'/{membership_type}/Profile/{membership_id}/',
            parameters=queries.Destiny2.GetProfile(components=components),
            response_format=responses.Destiny2.GetProfile
        )


def setup(client: Union[SyncClient, AsyncClient]) -> None:
    client.add_subclient(Destiny2())
