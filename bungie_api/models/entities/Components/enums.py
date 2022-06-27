from ..framework import DocumentedIntEnum


__all__ = [
    'ComponentPrivacySetting',
]


class ComponentPrivacySetting(DocumentedIntEnum):
    None_ = 0
    Public = 1
    Private = 2
