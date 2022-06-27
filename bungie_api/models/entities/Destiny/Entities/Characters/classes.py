from typing import (
    ForwardRef,
    List,
    Mapping,
    Optional
)

from arya_api_framework import BaseModel

from ......utils import ValidatedDatetime
from ....enums import BungieMembershipType
from ... import (
    Character,
    Milestones,
    Misc,
    Progression,
    HistoricalStats,
    Quests,
    Artifacts,
    DestinyClass,
    DestinyGender,
    DestinyRace,
    DestinyProgression,
    DyeReference,
    DestinyActivity,
)


DestinyItemPerksComponent = ForwardRef('Entities.Items.DestinyItemPerksComponent')


__all__ = [
    'DestinyCharacterComponent',
    'DestinyCharacterProgressionComponent',
    'DestinyCharacterRenderComponent',
    'DestinyCharacterActivitiesComponent',
]


class DestinyCharacterComponent(BaseModel):
    membershipId: int
    membershipType: BungieMembershipType
    characterId: int
    dateLastPlayed: ValidatedDatetime
    minutesPlayedThisSession: int
    minutesPlayedTotal: int
    light: int
    stats: Mapping[int, int]
    raceHash: int
    genderHash: int
    classHash: int
    raceType: DestinyRace
    classType: DestinyClass
    genderType: DestinyGender
    emblemPath: str
    emblemBackgroundPath: str
    emblemHash: int
    emblemColor: Misc.DestinyColor
    levelProgression: DestinyProgression
    baseCharacterLevel: int
    percentToNextLevel: float
    titleRecordHash: Optional[int]


class DestinyCharacterProgressionComponent(BaseModel):
    progressions: Mapping[int, DestinyProgression]
    factions: Mapping[int, Progression.DestinyFactionProgression]
    milestones: Mapping[int, Milestones.DestinyMilestone]
    quests: List[Quests.DestinyQuestStatus]
    uninstancedItemObjectives: Mapping[int, List[Quests.DestinyObjectiveProgress]]
    uninstancedItemPerks: Mapping[int, DestinyItemPerksComponent]
    checklists: Mapping[int, Mapping[int, bool]]
    seasonalArtifact: Artifacts.DestinyArtifactCharacterScoped


class DestinyCharacterRenderComponent(BaseModel):
    customDyes: List[DyeReference]
    customization: Character.DestinyCharacterCustomization
    peerView: Character.DestinyCharacterPeerView


class DestinyCharacterActivitiesComponent(BaseModel):
    dateActivityStarted: ValidatedDatetime
    availableActivities: List[DestinyActivity]
    currentActivityHash: int
    currentActivityModeHash: int
    currentActivityModeType: Optional[HistoricalStats.Definitions.DestinyActivityModeType]
    currentActivityModeHashes: Optional[List[int]]
    currentActivityModeTypes: Optional[List[HistoricalStats.Definitions.DestinyActivityModeType]]
    currentPlaylistActivityHash: Optional[int]
    lastCompletedStoryHash: int


from ... import Entities
