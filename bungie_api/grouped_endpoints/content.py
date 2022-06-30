from typing import (
    List,
    Optional,
    Union,
)

from arya_api_framework import SyncClient, AsyncClient, SubClient
from arya_api_framework.utils import apiclient, endpoint

from ..models import (
    responses,
    queries,
)


__all__ = [
    'Content'
]


@apiclient
class Content(SubClient, name='content', relative_path='/Content'):
    @endpoint(
        path='/Content/GetContentType/{type}/',
        name='Content.GetContentType',
        description='Gets an object describing a particular variant of content.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Content-GetContentType.html'
            '#operation_get_Content-GetContentType'
        ),
        method='GET'
    )
    def get_content_type(self, content_type: str) -> responses.Content.GetContentType:
        return self.get(
            f'/GetContentType/{content_type}',
            response_format=responses.Content.GetContentType
        )

    @endpoint(
        path='/Content/GetContentById/{id}/{locale}/',
        name='Content.GetContentById',
        description='Returns a content item referenced by id.',
        href=(
                'https://bungie-net.github.io/multi/operation_get_Content-GetContentById.html'
                '#operation_get_Content-GetContentById'
        ),
        method='GET'
    )
    def get_content_by_id(
            self,
            id: int,
            locale: str = 'en',
            head: bool = False
    ) -> responses.Content.GetContentById:
        return self.get(
            f'/GetContentById/{id}/{locale}/',
            parameters=queries.Content.GetContentById(head=head),
            response_format=responses.Content.GetContentById
        )

    @endpoint(
        path='/Content/GetContentByTagAndType/{tag}/{type}/{locale}/',
        name='Content.GetContentByTagAndType',
        description='Returns the newest item that matches a given tag and content type.',
        href=(
                'https://bungie-net.github.io/multi/operation_get_Content-GetContentByTagAndType.html'
                '#operation_get_Content-GetContentByTagAndType'
        ),
        method='GET'
    )
    def get_content_by_tag_and_type(
            self,
            tag: str,
            content_type: str,
            locale: str = 'en',
            head: bool = False
    ) -> responses.Content.GetContentByTagAndType:
        return self.get(
            f'/GetContentByTagAndType/{tag}/{content_type}/{locale}/',
            parameters=queries.Content.GetContentByTagAndType(head=head),
            response_format=responses.Content.GetContentByTagAndType
        )

    @endpoint(
        path='/Content/Search/{locale}/',
        name='Content.SearchContentWithText',
        description=(
                'Gets content based on querystring information passed in. Provides basic search and text search '
                'capabilities.'
        ),
        href=(
                'https://bungie-net.github.io/multi/operation_get_Content-SearchContentWithText.html'
                '#operation_get_Content-SearchContentWithText'
        ),
        method='GET'
    )
    def search_content_with_text(
            self,
            ctype: Union[str, List[str]],
            searchtext: Optional[str] = None,
            locale: Optional[str] = 'en',
            page: Optional[int] = 1,
            head: Optional[bool] = None,
            source: Optional[str] = None,
            tag: Optional[str] = None
    ) -> responses.Content.SearchContentWithText:
        return self.get(
            f'/Search/{locale}/',
            parameters=queries.Content.SearchContentWithText(
                ctype=ctype if not isinstance(ctype, list) else ' '.join(t.strip() for t in ctype),
                currentpage=page,
                head=head,
                searchtext=searchtext,
                source=source,
                tag=tag
            ),
            response_format=responses.Content.SearchContentWithText
        )

    @endpoint(
        path='/Content/SearchContentByTagAndType/{tag}/{type}/{locale}/',
        name='Content.SearchContentByTagAndType',
        description='Searches for content items that match th given tag and content type.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Content-SearchContentByTagAndType.html'
            '#operation_get_Content-SearchContentByTagAndType'
        ),
        method='GET'
    )
    def search_content_by_tag_and_type(
            self,
            tag: str,
            content_type: str,
            locale: Optional[str] = 'en',
            page: Optional[int] = 1,
            head: Optional[bool] = False,
            itemsperpage: Optional[int] = None
    ) -> responses.Content.SearchContentByTagAndType:
        return self.get(
            f'/SearchContentByTagAndType/{tag}/{content_type}/{locale}/',
            parameters=queries.Content.SearchContentByTagAndType(
                currentpage=page,
                head=head,
                itemsperpage=itemsperpage,
            ),
            response_format=responses.Content.SearchContentByTagAndType
        )

    @endpoint(
        path='/Content/SearchHelpArticles/{searchtext}/{size}/',
        name='Content.SearchHelpArticles',
        description=(
                'Search for help articles. NOTE: This endpoint seems to be unfinished, or at least not in use. '
                'I don\'t recommend trying to use it.'
        ),
        href=(
                'https://bungie-net.github.io/multi/operation_get_Content-SearchHelpArticles.html'
                '#operation_get_Content-SearchHelpArticles'
        ),
        method='GET'
    )
    def search_help_articles(self, searchtext: str, size: int) -> responses.BaseResponse:
        return self.get(
            f'/SearchHelpArticles/{searchtext}/{size}/',
            response_format=responses.BaseResponse
        )


def setup(client: Union[SyncClient, AsyncClient]):
    client.add_subclient(Content())
