from typing import TYPE_CHECKING
from typing import Optional

from arya_api_framework import SyncClient
from arya_api_framework.utils import apiclient, endpoint

from .utils import process_errors
from .models import responses, queries

if TYPE_CHECKING:
    from .grouped_endpoints.app import App
    from .grouped_endpoints.oauth import OAuth
    from .grouped_endpoints.user import User
    from .grouped_endpoints.content import Content
    from .grouped_endpoints.forum import Forum
    from .grouped_endpoints.groupv2 import GroupV2
    from .grouped_endpoints.tokens import Tokens
    from .grouped_endpoints.destiny2 import Destiny2
    from .grouped_endpoints.community_content import CommunityContent
    from .grouped_endpoints.trending import Trending
    from .grouped_endpoints.fireteam import Fireteam
    from .grouped_endpoints.social import Social


__all__ = [
    'BungieAPI',
]


API_ROOT = "https://www.bungie.net/Platform"
OAUTH_URL = "https://www.bungie.net/en/OAuth/Authorize"


@apiclient
class BungieAPI(
        SyncClient,
        uri=API_ROOT,
        extensions=[
            ('.grouped_endpoints.app', 'bungie_api'),
            ('.grouped_endpoints.oauth', 'bungie_api'),
            ('.grouped_endpoints.user', 'bungie_api'),
            ('.grouped_endpoints.content', 'bungie_api'),
            ('.grouped_endpoints.forum', 'bungie_api'),
            ('.grouped_endpoints.groupv2', 'bungie_api'),
            ('.grouped_endpoints.tokens', 'bungie_api'),
            ('.grouped_endpoints.destiny2', 'bungie_api'),
            ('.grouped_endpoints.community_content', 'bungie_api'),
            ('.grouped_endpoints.trending', 'bungie_api'),
            ('.grouped_endpoints.fireteam', 'bungie_api'),
            ('.grouped_endpoints.social', 'bungie_api'),
        ],
        error_responses={
            403: process_errors,
            500: process_errors,
            503: process_errors,
        },
        rate_limit=5,
):
    app: 'App'
    oauth: 'OAuth'
    user: 'User'
    content: 'Content'
    forum: 'Forum'
    groupv2: 'GroupV2'
    tokens: 'Tokens'
    destiny2: 'Destiny2'
    community_content: 'CommunityContent'
    trending: 'Trending'
    fireteam: 'Fireteam'
    social: 'Social'

    api_key: str
    client_id: Optional[int]

    oauth_url: str = OAUTH_URL

    def __init__(self, api_key: str, client_id: Optional[int] = None) -> None:
        self.api_key = api_key
        self.client_id = client_id

        self.headers['X-API-Key'] = self.api_key

    @endpoint(
        path='/GetAvailableLocales/',
        name='GetAvailableLocales',
        description='List of available localization cultures.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_-GetAvailableLocales.html'
            '#operation_get_-GetAvailableLocales'
        ),
        method='GET'
    )
    def get_available_locales(self) -> responses.GetAvailableLocales:
        return self.get(
            '/GetAvailableLocales/',
            response_format=responses.GetAvailableLocales
        )

    @endpoint(
        path='/Settings/',
        name='GetCommonSettings',
        description='Get the common settings used by the Bungie.net environment.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_-GetCommonSettings.html#operation_get_-GetCommonSettings'
        ),
        method='GET'
    )
    def get_common_settings(self) -> responses.GetCommonSettings:
        return self.get(
            '/Settings/',
            response_format=responses.GetCommonSettings
        )

    @endpoint(
        path='/UserSystemOverrides/',
        name='GetUserSystemOverrides',
        description='Get the user-specific system overrides that should be respected alongside common systems.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_-GetUserSystemOverrides.html'
            '#operation_get_-GetUserSystemOverrides'
        ),
        method='GET'
    )
    def get_user_system_overrides(self) -> responses.GetUserSystemOverrides:
        return self.get(
            '/UserSystemOverrides/',
            response_format=responses.GetUserSystemOverrides
        )

    @endpoint(
        path='/GlobalAlerts/',
        name='GetGlobalAlerts',
        description=(
            'Gets any active global alert for display in the forum banners, help pages, etc. Usually used for DOC '
            'alerts.'
        ),
        href='https://bungie-net.github.io/multi/operation_get_-GetGlobalAlerts.html#operation_get_-GetGlobalAlerts',
        method='GET'
    )
    def get_global_alerts(self, include_streaming: Optional[bool] = None) -> responses.GetGlobalAlerts:
        return self.get(
            '/GlobalAlerts/',
            parameters=queries.GetGlobalAlerts(includestreaming=include_streaming),
            response_format=responses.GetGlobalAlerts
        )
