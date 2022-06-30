from ...framework import DocumentedIntEnum


__all__ = [
    'AwaType',
]


class AwaType(DocumentedIntEnum):
    None_ = 0
    InsertPlugs = 1, 'Insert plugs into sockets.'
