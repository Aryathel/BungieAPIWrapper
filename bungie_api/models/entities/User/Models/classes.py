from typing import Optional

from arya_api_framework import BaseModel

from .enums import BungieCredentialType


__all__ = [
    'GetCredentialTypesForAccountResponse',
]


class GetCredentialTypesForAccountResponse(BaseModel):
    credentialType: BungieCredentialType
    credentialDisplayName: str
    isPublic: bool
    credentialAsString: Optional[str]
