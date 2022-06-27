from typing import (
    Any,
    Union,
)

from arya_api_framework import SubClient, SyncClient, AsyncClient
from arya_api_framework.utils import apiclient, endpoint

from ..decorators import destinyclient, oauth_required
from ..errors import ObsoleteError
from ..models.entities.Applications import ApplicationScopes
from ..models.entities import BungieMembershipType
from ..models.entities.User.Models import BungieCredentialType
from ..models import responses
from ..models import queries


@destinyclient
@apiclient
class User(SubClient, name='user', relative_path='/User'):
    @oauth_required(ApplicationScopes.ReadBasicUserProfile)
    @endpoint(
        path='/User/GetCurrentBungieNetUser/',
        name='User.GetCurrentBungieNetUser',
        description='Gets information about the user represented by the currently authenticated bearer token.',
        method='GET'
    )
    def get_current_bungie_net_user(self) -> responses.User.GetCurrentBungieNetUser:
        return self.get(
            '/GetCurrentBungieNetUser/',
            response_format=responses.User.GetCurrentBungieNetUser
        )

    @endpoint(
        path='/User/GetBungieNetUserById/{id}/',
        name='User.GetbungieNetUserById',
        description='Loads a Bungie.net user by their membership id.',
        href='https://bungie-net.github.io/multi/operation_get_User-GetBungieNetUserById.html#operation_get_User-GetBungieNetUserById',
        method='GET'
    )
    def get_bungie_net_user_by_id(self, id: int) -> responses.User.GetBungieNetUserById:
        return self.get(
            f'/GetBungieNetUserById/{id}',
            response_format=responses.User.GetBungieNetUserById
        )

    @endpoint(
        path='/User/GetSanitizedPlatformDisplayNames/{membershipId}/',
        name='User.GetSanitizedPlatformDisplayNames',
        description=(
                'Gets a list of all display names linked to this membership id but sanitized (profanity filtered). '
                'Obeys all visibility rules of the calling user and is heavily cached.'
        ),
        href='https://bungie-net.github.io/multi/operation_get_User-GetSanitizedPlatformDisplayNames.html#operation_get_User-GetSanitizedPlatformDisplayNames',
        method='GET'
    )
    def get_sanitized_platform_display_names(
            self,
            membership_id: int
    ) -> responses.User.GetSanitizedPlatformDisplayNames:
        """
        Gets a list of all display names linked to this membership id but sanitized (profanity filtered).
        Obeys all visibility rules of the calling user and is heavily cached.

        Arguments
        ---------
            membership_id: :py:class:`int`
                The membership id of the Bungie.net user to fetch sanitized names for.

        Returns
        -------
            :class:`responses.User.SanitizedPlatformDisplayNames`
        """

        return self.get(
            f'/GetSanitizedPlatformDisplayNames/{membership_id}/',
            response_format=responses.User.GetSanitizedPlatformDisplayNames
        )

    @endpoint(
        path='/User/GetCredentialTypesForTargetAccount/{membershipId}/',
        name='User.GetCredentialTypesForTargetAccount',
        description='Returns a list of credential types attached to the requested account.',
        href='https://bungie-net.github.io/multi/operation_get_User-GetCredentialTypesForTargetAccount.html#operation_get_User-GetCredentialTypesForTargetAccount',
        method='GET'
    )
    def get_credential_types_for_target_account(
            self,
            membership_id: int
    ) -> responses.User.GetCredentialTypesForTargetAccount:
        return self.get(
            f'/GetCredentialTypesForTargetAccount/{membership_id}/',
            response_format=responses.User.GetCredentialTypesForTargetAccount
        )

    @endpoint(
        path='/User/GetAvailableThemes/',
        name='User.GetAvailableThemes',
        description='Returns a list of all available user themes.',
        href='https://bungie-net.github.io/multi/operation_get_User-GetAvailableThemes.html#operation_get_User-GetAvailableThemes',
        method='GET'
    )
    def get_available_themes(self) -> responses.User.GetAvailableThemes:
        return self.get('/GetAvailableThemes/', response_format=responses.User.GetAvailableThemes)

    @endpoint(
        path='/User/GetMembershipsById/{membershipId}/{membershipType}/',
        name='User.GetMembershipDataById',
        description=(
            'Returns a list of accounts associated with the supplied membership ID and membership type. This will '
            'include all linked accounts (even when hidden) if supplied credentials permit it.'
        ),
        href='https://bungie-net.github.io/multi/operation_get_User-GetMembershipDataById.html#operation_get_User-GetMembershipDataById',
        method='GET'
    )
    def get_memberships_by_id(
            self,
            membership_id: int,
            membership_type: Union[int, BungieMembershipType]
    ) -> responses.User.GetMembershipDataById:
        if isinstance(membership_type, int):
            membership_type = BungieMembershipType(membership_type)
        return self.get(
            f'/GetMembershipsById/{membership_id}/{membership_type.value}/',
            response_format=responses.User.GetMembershipDataById
        )

    @oauth_required(ApplicationScopes.ReadBasicUserProfile)
    @endpoint(
        path='/User/GetMembershipsForCurrentUser/',
        name='User.GetMembershipDataForCurrentUser',
        description=(
            'Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that '
            'do not give you access to the token response.'
        ),
        href='https://bungie-net.github.io/multi/operation_get_User-GetMembershipDataForCurrentUser.html#operation_get_User-GetMembershipDataForCurrentUser',
        method='GET'
    )
    def get_memberships_for_current_user(self) -> responses.User.GetMembershipDataForCurrentUser:
        return self.get(
            '/GetMembershipsForCurrentUser/',
            response_format=responses.User.GetMembershipDataForCurrentUser
        )

    @endpoint(
        path='/User/GetMembershipFromHardLinkedCredential/{crType}/{credential}/',
        name='User.GetMembershipFromHardLinkedCredential',
        description=(
            'Gets any hard linked membership given a credential. Only works for credentials that are public '
            '(just SteamID64 right now). Cross Save aware.'
        ),
        href='https://bungie-net.github.io/multi/operation_get_User-GetMembershipFromHardLinkedCredential.html#operation_get_User-GetMembershipFromHardLinkedCredential',
        method='GET'
    )
    def get_membership_from_hard_linked_credential(
            self,
            credential: Any,
            credential_type: Union[str, int, BungieCredentialType] = BungieCredentialType.SteamId
    ) -> responses.User.GetMembershipFromHardLinkedCredential:
        if isinstance(credential_type, int):
            credential_type = BungieCredentialType(credential_type)
        elif isinstance(credential_type, str):
            credential_type = getattr(BungieCredentialType, credential_type, None)
            if not credential_type:
                raise ValueError('The "credential_type" is not a recognized BungieCredentialType.')

        return self.get(
            f'/GetMembershipFromHardLinkedCredential/{credential_type.name}/{credential}/',
            response_format=responses.User.GetMembershipFromHardLinkedCredential
        )

    @endpoint(
        path='/User/Search/Prefix/{displayNamePrefix}/{page}/',
        name='User.SearchByGlobalNamePrefix',
        description='[OBSOLETE] Do not use this to search users, use SearchByGlobalNamePost instead.',
        href='https://bungie-net.github.io/multi/operation_get_User-SearchByGlobalNamePrefix.html#operation_get_User-SearchByGlobalNamePrefix',
        method='GET'
    )
    def search_by_global_name_prefix(self) -> None:
        raise ObsoleteError('Do not use this to search users, use "search_by_global_name_post" instead.')

    @endpoint(
        path='/User/Search/GlobalName/{page}/',
        name='User.SearchByGlobalNamePost',
        description='Given the prefix of a global display name, returns all users who share that name.',
        href='https://bungie-net.github.io/multi/operation_post_User-SearchByGlobalNamePost.html#operation_post_User-SearchByGlobalNamePost',
        method='POST'
    )
    def search_by_global_name_post(
            self,
            display_name_prefix: str,
            page: int = 0
    ) -> responses.User.SearchByGlobalNamePost:
        return self.post(
            f'/Search/GlobalName/{page}',
            body=queries.User.UserSearchPrefixRequest(displayNamePrefix=display_name_prefix),
            response_format=responses.User.SearchByGlobalNamePost
        )


def setup(client: Union[SyncClient, AsyncClient]) -> None:
    client.add_subclient(User())
