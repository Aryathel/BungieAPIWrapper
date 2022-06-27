from arya_api_framework import BaseModel


__all__ = [
    'DestinyPerkReference',
]


class DestinyPerkReference(BaseModel):
    perkHash: int
    iconPath: str
    isActive: bool
    visible: bool
