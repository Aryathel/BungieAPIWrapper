from typing import Optional

from arya_api_framework import Response


__all__ = [
    'Token',
]


class Token(Response):
    access_token: str
    token_type: str
    expires_in: int
    membership_id: int
    refresh_token: Optional[str]
    refresh_expires_in: Optional[int]
