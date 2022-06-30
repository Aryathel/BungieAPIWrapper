from functools import wraps
from typing import (
    Any,
    Callable,
)

from arya_api_framework import SyncClient, AsyncClient, SubClient
from arya_api_framework.errors import ClientError

from .models.entities import Applications


__all__ = [
    'destinyclient',
    'oauth_required',
]


# ==================
#    Decorators
# ==================
def destinyclient(cls):
    if '__endpoints__' not in cls.__dict__:
        cls.__endpoints__ = {}

    for name, method in cls.__dict__.items():
        if hasattr(method, '__requires_oauth__') and getattr(method, '__requires_oauth__'):
            if method.__name__ not in cls.__endpoints__:
                cls.__endpoints__[method.__name__] = {}
            cls.__endpoints__[method.__name__]['oauth_scopes'] = method.__oauth_scopes__

    return cls


def oauth_required(
        scopes: Applications.ApplicationScopes = None
) -> Callable[..., Callable[..., Any]]:
    if scopes:
        scopes = Applications.ApplicationScopes.members(scopes)

    def callback(func: Callable[..., Any]) -> Callable[..., Any]:
        func.__requires_oauth__ = True
        func.__oauth_scopes__ = scopes

        @wraps(func)
        def internal(self, *args, **kwargs):
            cl = self
            if isinstance(cl, SubClient):
                cl = self.root

            root = None
            if isinstance(cl, SyncClient) or isinstance(cl, AsyncClient):
                root = self.root.bearer_token

            if root:
                return func(self, *args, **kwargs)

            raise ClientError(
                f'The "{func.__name__}" endpoint must be used after an oauth action has been performed.'
            )

        return internal

    return callback
