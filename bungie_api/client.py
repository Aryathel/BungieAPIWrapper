from typing import TYPE_CHECKING
from typing import Optional

from arya_api_framework import SyncClient

from . import models

from .utils import process_errors

if TYPE_CHECKING:
    from .grouped_endpoints.app import App
    from .grouped_endpoints.oauth import OAuth
    from .grouped_endpoints.user import User
    from .grouped_endpoints.content import Content
    from .grouped_endpoints.forum import Forum
    from .grouped_endpoints.groupv2 import GroupV2
    from .grouped_endpoints.tokens import Tokens
    from .grouped_endpoints.destiny2 import Destiny2


__all__ = [
    'BungieAPI',
]


API_ROOT = "https://www.bungie.net/Platform"
OAUTH_URL = "https://www.bungie.net/en/OAuth/Authorize"


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

    api_key: str
    client_id: Optional[int]

    oauth_url: str = OAUTH_URL

    def __init__(self, api_key: str, client_id: Optional[int] = None) -> None:
        self.api_key = api_key
        self.client_id = client_id

        self.headers['X-API-Key'] = self.api_key
