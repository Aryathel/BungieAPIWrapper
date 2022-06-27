from typing import List

from .. import entities
from .framework import BaseResponse


__all__ = [
    'GetDestinyManifest',
    'GetDestinyEntityDefinition',
    'SearchDestinyPlayerByBungieName',
    'GetLinkedProfiles',
]


class GetDestinyManifest(BaseResponse):
    Response: entities.Destiny.Config.DestinyManifest


class GetDestinyEntityDefinition(BaseResponse):
    Response: entities.Destiny.Definitions.DestinyDefinition


class SearchDestinyPlayerByBungieName(BaseResponse):
    Response: List[entities.User.UserInfoCard]


class GetLinkedProfiles(BaseResponse):
    Response: entities.Destiny.Responses.DestinyLinkedProfileResponse


class GetProfile(BaseResponse):
    Response: entities.Destiny.Responses.DestinyProfileResponse
