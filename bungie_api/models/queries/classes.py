from typing import Optional

from arya_api_framework import BaseModel


__all__ = [
    'GetGlobalAlerts',
]


class GetGlobalAlerts(BaseModel):
    includestreaming: Optional[bool]
