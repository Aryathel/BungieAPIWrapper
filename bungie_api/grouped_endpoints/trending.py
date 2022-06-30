from typing import (
    Optional,
    Union,
)

from arya_api_framework import SyncClient, AsyncClient, SubClient
from arya_api_framework.utils import apiclient, endpoint

from ..models import responses, entities


__all__ = [
    'Trending'
]


TrendingEntryType = Union[int, str, entities.Trending.TrendingEntryType]


@apiclient
class Trending(SubClient, name='trending', relative_path='/Trending/'):
    @endpoint(
        path='/Trending/Categories/',
        name='Trending.GetTrendingCategories',
        description=(
            'Returns trending items for Bungie.net, collapsed into the first page of items per category. For '
            'pagination within a category, call GetTrendingCategory.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Trending-GetTrendingCategories.html'
            '#operation_get_Trending-GetTrendingCategories'
        ),
        method='GET'
    )
    def get_trending_categories(self) -> responses.Trending.GetTrendingCategories:
        return self.get(
            '/Categories/',
            response_format=responses.Trending.GetTrendingCategories
        )

    @endpoint(
        path='/Trending/Categories/{categoryId}/{pageNumber}/',
        name='Trending.GetTrendingCategory',
        description='Returns a paginated list of trending items for a category.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Trending-GetTrendingCategory.html'
            '#operation_get_Trending-GetTrendingCategory'
        ),
        method='GET'
    )
    def get_trending_category(
            self,
            category_id: str,
            page: Optional[int] = 0
    ) -> responses.Trending.GetTrendingCategory:
        return self.get(
            f'/Categories/{category_id}/{page}/',
            response_format=responses.Trending.GetTrendingCategory
        )

    @endpoint(
        path='/Trending/Details/{trendingEntryType}/{identifier}/',
        name='Trending.GetTrendingEntryDetail',
        description=(
            'Returns the detailed results for a specific trending entry. Note that trending entries are uniquely '
            'identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is '
            'not guaranteed to be globally unique.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Trending-GetTrendingEntryDetail.html'
            '#operation_get_Trending-GetTrendingEntryDetail'
        ),
        method='GET'
    )
    def get_trending_entry_detail(
            self,
            trending_entry_id: Union[int, str],
            trending_entry_type: TrendingEntryType
    ) -> responses.Trending.GetTrendingEntryDetail:
        trending_entry_type = entities.Trending.TrendingEntryType.int_validator(trending_entry_type)
        
        return self.get(
            f'/Details/{trending_entry_type}/{trending_entry_id}/',
            response_format=responses.Trending.GetTrendingEntryDetail
        )


def setup(client: Union[SyncClient, AsyncClient]) -> None:
    client.add_subclient(Trending())
