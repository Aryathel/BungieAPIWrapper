from arya_api_framework import BaseModel


__all__ = [
    'UserSearchPrefixRequest',
    'ExactSearchRequest',
]


class UserSearchPrefixRequest(BaseModel):
    displayNamePrefix: str


class ExactSearchRequest(BaseModel):
    displayName: str
    displayNameCode: int
