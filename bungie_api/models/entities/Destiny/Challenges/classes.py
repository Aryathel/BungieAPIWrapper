from arya_api_framework import BaseModel

from .. import Quests


__all__ = [
    'DestinyChallengeStatus',
]


class DestinyChallengeStatus(BaseModel):
    objective: Quests.DestinyObjectiveProgress
