from typing import (
    Optional,
    Union,
)

from arya_api_framework import SyncClient, AsyncClient, SubClient
from arya_api_framework.utils import apiclient, endpoint

from ..models import responses
from ..models.entities import Forum


CCSortType = Union[int, str, Forum.CommunityContentSortMode]
MediaType = Union[int, str, Forum.ForumMediaType]


__all__ = [
    'CommunityContent'
]


@apiclient
class CommunityContent(SubClient, name='community_content', relative_path='/CommunityContent/'):
    @endpoint(
        path='/CommunityContent/Get/{sort}/{mediaFilter}/{page}/',
        name='CommunityContent.GetCommunityContent',
        description='Returns community content.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_CommunityContent-GetCommunityContent.html'
            '#operation_get_CommunityContent-GetCommunityContent'
        ),
        method='GET'
    )
    def get_community_content(
            self,
            sort: Optional[CCSortType] = Forum.CommunityContentSortMode.Trending,
            media_filter: Optional[MediaType] = Forum.ForumMediaType.None_,
            page: Optional[int] = 0,
    ) -> responses.CommunityContent.GetCommunityContent:
        sort = Forum.CommunityContentSortMode.int_validator(sort)
        media_filter = Forum.ForumMediaType.int_validator(media_filter)

        return self.get(
            f'/Get/{sort}/{media_filter}/{page}/',
            response_format=responses.CommunityContent.GetCommunityContent
        )


def setup(client: Union[SyncClient, AsyncClient]) -> None:
    client.add_subclient(CommunityContent())
