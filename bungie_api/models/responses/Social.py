from ..entities import Social
from .framework import BaseResponse


__all__ = [
    'GetFriendList',
    'GetFriendRequestList',
    'IssueFriendRequest',
    'AcceptFriendRequest',
    'DeclineFriendRequest',
    'RemoveFriend',
    'RemoveFriendRequest',
]


class GetFriendList(BaseResponse):
    Response: Social.Friends.BungieFriendListResponse


class GetFriendRequestList(BaseResponse):
    Response: Social.Friends.BungieFriendRequestListResponse


class IssueFriendRequest(BaseResponse):
    Response: bool


class AcceptFriendRequest(BaseResponse):
    Response: bool


class DeclineFriendRequest(BaseResponse):
    Response: bool


class RemoveFriend(BaseResponse):
    Response: bool


class RemoveFriendRequest(BaseResponse):
    Response: bool


class GetPlatformFriendList(BaseResponse):
    Response: Social.Friends.PlatformFriendResponse
