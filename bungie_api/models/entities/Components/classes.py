from typing import Optional

from arya_api_framework import BaseModel

from .enums import ComponentPrivacySetting


__all__ = [
    'ComponentResponse',
]


class ComponentResponse(BaseModel):
    privacy: ComponentPrivacySetting
    disabled: Optional[bool]
