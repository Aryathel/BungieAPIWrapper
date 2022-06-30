from typing import (
    Optional,
    Union,
)

from arya_api_framework import SyncClient, AsyncClient, SubClient
from arya_api_framework.utils import apiclient, endpoint

from ..decorators import destinyclient, oauth_required
from ..models import responses
from ..models.entities.Social import Friends
from ..models.entities.Applications import ApplicationScopes


__all__ = [
    'Social'
]


PlatformType = Union[int, str, Friends.PlatformFriendType]


@destinyclient
@apiclient
class Social(SubClient, name='social', relative_path='/Social/'):
    @oauth_required(ApplicationScopes.ReadUserData)
    @endpoint(
        path='/Social/Friends/',
        name='Social.GetFriendList',
        description='Returns your Bungie friends list.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Social-GetFriendList.html'
            '#operation_get_Social-GetFriendList'
        ),
        method='GET'
    )
    def get_friend_list(self) -> responses.Social.GetFriendList:
        return self.get(
            '/Friends/',
            response_format=responses.Social.GetFriendList
        )

    @oauth_required(ApplicationScopes.ReadUserData)
    @endpoint(
        path='/Social/Friends/Requests/',
        name='Social.GetFriendRequestList',
        description='Returns your friend request queue.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Social-GetFriendRequestList.html'
            '#operation_get_Social-GetFriendRequestList'
        ),
        method='GET'
    )
    def get_friend_request_list(self) -> responses.Social.GetFriendRequestList:
        return self.get(
            '/Friends/Requests/',
            response_format=responses.Social.GetFriendRequestList
        )

    @oauth_required(ApplicationScopes.BnetWrite)
    @endpoint(
        path='/Social/Friends/Add/{membershipId}/',
        name='Social.IssueFriendRequest',
        description=(
                'Requests a friend relationship with the target user. Any of the target user\'s linked membership ids '
                'are valid inputs.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Social-IssueFriendRequest.html'
            '#operation_post_Social-IssueFriendRequest'
        ),
        method='POST'
    )
    def issue_friend_request(self, membership_id: int) -> responses.Social.IssueFriendRequest:
        return self.post(
            f'/Friends/Add/{membership_id}/',
            response_format=responses.Social.IssueFriendRequest
        )

    @oauth_required(ApplicationScopes.BnetWrite)
    @endpoint(
        path='/Social/Friends/Requests/Accept/{membershipId}/',
        name='Social.AcceptFriendRequest',
        description=(
            'Accepts a friend relationship with the target user. The user must be on your incoming friend request '
            'list, though no error will occur if they are not.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Social-AcceptFriendRequest.html'
            '#operation_post_Social-AcceptFriendRequest'
        ),
        method='POST'
    )
    def accept_friend_request(self, membership_id: int) -> responses.Social.AcceptFriendRequest:
        return self.post(
            f'/Friends/Requests/Accept/{membership_id}/',
            response_format=responses.Social.AcceptFriendRequest
        )

    @oauth_required(ApplicationScopes.BnetWrite)
    @endpoint(
        path='/Social/Friends/Requests/Decline/{membershipId}/',
        name='Social.DeclineFriendRequest',
        description=(
            'Declines a friend relationship with the target user. The user must be on your incoming friend request '
            'list, though no error will occur if they are not.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Social-DeclineFriendRequest.html'
            '#operation_post_Social-DeclineFriendRequest'
        ),
        method='POST'
    )
    def decline_friend_request(self, membership_id: int) -> responses.Social.DeclineFriendRequest:
        return self.post(
            f'/Friends/Requests/Decline/{membership_id}/',
            response_format=responses.Social.DeclineFriendRequest
        )

    @oauth_required(ApplicationScopes.BnetWrite)
    @endpoint(
        path='/Social/Friends/Remove/{membershipId}/',
        name='Social.RemoveFriend',
        description=(
                'Remove a friend relationship with the target user. The user must be on your friend list, though no '
                'error will occur if they are not.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Social-RemoveFriend.html'
            '#operation_post_Social-RemoveFriend'
        ),
        method='POST'
    )
    def remove_friend(self, membership_id: int) -> responses.Social.RemoveFriend:
        return self.post(
            f'/Friends/Remove/{membership_id}/',
            response_format=responses.Social.RemoveFriend
        )

    @oauth_required(ApplicationScopes.BnetWrite)
    @endpoint(
        path='/Social/Friends/Requests/Remove/{membershipId}/',
        name='Social.RemoveFriendRequest',
        description=(
            'Remove a friend relationship with the target user. The user must be on your outgoing request friend list, '
            'though no error will occur if they are not.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Social-RemoveFriendRequest.html'
            '#operation_post_Social-RemoveFriendRequest'
        ),
        method='POST'
    )
    def remove_friend_request(self, membership_id: int) -> responses.Social.RemoveFriendRequest:
        return self.post(
            f'/Friends/Requests/Remove/{membership_id}/',
            response_format=responses.Social.RemoveFriendRequest
        )

    @oauth_required()
    @endpoint(
        path='/Social/PlatformFriends/{friendPlatform}/{page}/',
        name='Social.GetPlatformFriendList',
        description=(
            'Gets the platform friend of the requested type, with additional information if they have Bungie accounts. '
            'Must have a recent login session with said platform.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Social-GetPlatformFriendList.html'
            '#operation_get_Social-GetPlatformFriendList'
        ),
        method='GET'
    )
    def get_platform_friend_list(
            self,
            platform: PlatformType,
            page: Optional[int] = 0
    ) -> responses.Social.GetPlatformFriendList:
        platform = Friends.PlatformFriendType.int_validator(platform)

        return self.get(
            f'/PlatformFriends/{platform}/{page}/',
            response_format=responses.Social.GetPlatformFriendList
        )


def setup(client: Union[SyncClient, AsyncClient]) -> None:
    client.add_subclient(Social())
