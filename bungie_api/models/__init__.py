from . import entities
from . import responses
from . import queries


__all__ = [
    'responses',
    'queries',
    'entities',
]


def update_forward_refs():
    entities.User.UserMembershipData.update_forward_refs()

    entities.GroupsV2.GroupMember.update_forward_refs()
    entities.GroupsV2.GroupPotentialMember.update_forward_refs()
    entities.GroupsV2.GroupBan.update_forward_refs()
    entities.GroupsV2.GroupMemberApplication.update_forward_refs()
    entities.GroupsV2.GroupApplicationListRequest.update_forward_refs()

    entities.Destiny.Entities.Profiles.DestinyProfileComponent.update_forward_refs()
    entities.Destiny.Entities.Characters.DestinyCharacterProgressionComponent.update_forward_refs()

    entities.Destiny.Definitions.DestinyItemValueBlockDefinition.update_forward_refs()
    entities.Destiny.Definitions.DestinyItemTranslationBlockDefinition.update_forward_refs()
    entities.Destiny.Definitions.DestinyEntitySearchResult.update_forward_refs()

    entities.Destiny.Definitions.Records.DestinyRecordIntervalRewards.update_forward_refs()
    entities.Destiny.Definitions.Records.DestinyRecordDefinition.update_forward_refs()

    entities.Destiny.Definitions.Sources.DestinyItemSourceDefinition.update_forward_refs()

    entities.Destiny.HistoricalStats.DestinyPlayer.update_forward_refs()

    entities.Destiny.Responses.DestinyLinkedProfileResponse.update_forward_refs()
    entities.Destiny.Responses.DestinyErrorProfiles.update_forward_refs()
    entities.Destiny.Responses.DestinyProfileUserInfoCard.update_forward_refs()
    entities.Destiny.Responses.DestinyProfileResponse.update_forward_refs()
    entities.Destiny.Responses.DestinyCharacterResponse.update_forward_refs()
    entities.Destiny.Responses.DestinyItemResponse.update_forward_refs()
    entities.Destiny.Responses.DestinyVendorsResponse.update_forward_refs()
    entities.Destiny.Responses.DestinyVendorResponse.update_forward_refs()
    entities.Destiny.Responses.DestinyPublicVendorsResponse.update_forward_refs()
    entities.Destiny.Responses.DestinyCollectibleNodeDetailResponse.update_forward_refs()

    entities.Destiny.Components.Inventory.DestinyPlatformSilverComponent.update_forward_refs()

    entities.Trending.TrendingCategory.update_forward_refs()

    entities.Fireteam.FireteamMember.update_forward_refs()
