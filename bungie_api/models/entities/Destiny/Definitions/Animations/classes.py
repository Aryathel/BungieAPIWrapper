from arya_api_framework import BaseModel


__all__ = [
    'DestinyAnimationReference',
]


class DestinyAnimationReference(BaseModel):
    animName: str
    animIdentifier: str
    path: str
