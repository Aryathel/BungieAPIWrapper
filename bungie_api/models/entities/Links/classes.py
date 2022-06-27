from arya_api_framework import BaseModel


__all__ = [
    'HyperlinkReference',
]


class HyperlinkReference(BaseModel):
    title: str
    url: str
