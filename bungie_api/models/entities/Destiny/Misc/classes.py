from arya_api_framework import BaseModel


__all__ = [
    'DestinyColor'
]


class DestinyColor(BaseModel):
    red: int
    green: int
    blue: int
    alpha: int
