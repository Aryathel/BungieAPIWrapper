from ..framework import DocumentedIntFlag


__all__ = [
    'OptInFlags',
]


class OptInFlags(DocumentedIntFlag):
    None_ = 0
    Newsletter = 1
    System = 2
    Marketing = 4
    UserResearch = 8
    CustomerService = 16
    Social = 32
    PlayTests = 64
    PlayTestsLocal = 128
    Careers = 256
