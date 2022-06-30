from typing import (
    List,
    Optional,
    Union,
    TYPE_CHECKING
)

from arya_api_framework import SyncClient, AsyncClient, SubClient
from arya_api_framework.utils import apiclient, endpoint

from ..decorators import destinyclient, oauth_required
from ..models import responses, queries
from ..models.entities import (
    BungieMembershipType,
    Destiny,
)
from ..models.entities.Applications import ApplicationScopes

if TYPE_CHECKING:
    from datetime import datetime


__all__ = [
    'Destiny2'
]


MemberType = Union[int, str, BungieMembershipType]
VendorFilter = Union[int, str, Destiny.DestinyVendorFilter]
ComponentType = Union[int, str, Destiny.DestinyComponentType]
SocketArrayType = Union[int, str, Destiny.Requests.Actions.DestinySocketArrayType]
ActivityModeType = Union[int, str, Destiny.HistoricalStats.Definitions.DestinyActivityModeType]
StatsGroupType = Union[int, str, Destiny.HistoricalStats.Definitions.DestinyStatsGroupType]
PeriodType = Union[int, str, Destiny.HistoricalStats.Definitions.PeriodType]
AwaType = Union[int, str, Destiny.Advanced.AwaType]


@destinyclient
@apiclient
class Destiny2(SubClient, name='destiny2', relative_path='/Destiny2'):
    @endpoint(
        path='/Destiny2/Manifest/',
        name='Destiny2.GetDestinyManifest',
        description='Returns the current version of the manifest as a JSON object.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetDestinyManifest.html'
            '#operation_get_Destiny2-GetDestinyManifest'
        ),
        method='GET'
    )
    def get_destiny_manifest(self) -> responses.Destiny2.GetDestinyManifest:
        return self.get(
            '/Manifest/',
            response_format=responses.Destiny2.GetDestinyManifest
        )

    @endpoint(
        path='/Destiny2/Manifest/{entityType}/{hashIdentifier}/',
        name='Destiny2.GetDestinyEntityDefinition',
        description=(
            'Returns the static definition of an entity of the given Type and hash identifier. Examine the API '
            'Documentation for the Type Names of entities that have their own definitions. Note that the return '
            'type will always *inherit from* DestinyDefinition, but the specific type returned will be the requested '
            'entity type if it can be found. Please don\'t use this as a chatty alternative to the Manifest database '
            'if you require large sets of data, but for simple and one-off accesses this should be handy.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetDestinyEntityDefinition.html'
            '#operation_get_Destiny2-GetDestinyEntityDefinition'
        ),
        method='GET'
    )
    def get_destiny_entity_definition(
            self,
            entity_type: str,
            hash_identifier: int
    ) -> responses.Destiny2.GetDestinyEntityDefinition:
        return self.get(
            f'/Manifest/{entity_type}/{hash_identifier}/',
            response_format=responses.Destiny2.GetDestinyEntityDefinition
        )

    @endpoint(
        path='/Destiny2/SearchDestinyPlayerByBungieName/{membershipType}/',
        name='Destiny2.SearchDestinyPlayerByBungieName',
        description=(
            'Returns a list of Destiny memberships given a global Bungie Display Name. This method will hide '
            'overridden memberships due to cross save.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Destiny2-SearchDestinyPlayerByBungieName.html'
            '#operation_post_Destiny2-SearchDestinyPlayerByBungieName'
        ),
        method='POST'
    )
    def search_destiny_player_by_bungie_name(
            self,
            display_name: str,
            display_name_code: int,
            membership_type: MemberType
    ) -> responses.Destiny2.SearchDestinyPlayerByBungieName:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.post(
            f'/SearchDestinyPlayerByBungieName/{membership_type}',
            body=queries.User.ExactSearchRequest(
                displayName=display_name,
                displayNameCode=display_name_code
            ),
            response_format=responses.Destiny2.SearchDestinyPlayerByBungieName
        )

    @endpoint(
        path='/Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/',
        name='Destiny2.GetLinkedProfiles',
        description=(
            'Returns a summary information about all profiles linked to the requesting membership type/membership ID '
            'that have valid Destiny information. The passed-in Membership Type/Membership ID may be a Bungie.Net '
            'membership or a Destiny membership. It only returns the minimal amount of data to begin making more '
            'substantive requests, but will hopefully serve as a useful alternative to UserServices for people who '
            'just care about Destiny data. Note that it will only return linked accounts whose linkages you are '
            'allowed to view.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetLinkedProfiles.html'
            '#operation_get_Destiny2-GetLinkedProfiles'
        ),
        method='GET'
    )
    def get_linked_profiles(
            self,
            membership_id: int,
            membership_type: MemberType,
            get_all_memberships: Optional[bool] = None
    ) -> responses.Destiny2.GetLinkedProfiles:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.get(
            f'/{membership_type}/Profile/{membership_id}/LinkedProfiles/',
            parameters=queries.Destiny2.GetLinkedProfiles(getAllMemberships=get_all_memberships),
            response_format=responses.Destiny2.GetLinkedProfiles
        )

    @endpoint(
        path='/Destiny2/{membershipType}/Profile/{destinyMembershipId}/',
        name='Destiny2.GetProfile',
        description='Returns the destiny profile information for the supplied membership.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetProfile.html'
            '#operation_get_Destiny2-GetProfile'
        ),
        method='GET'
    )
    def get_profile(
            self,
            membership_id: int,
            membership_type: MemberType,
            components: Union[ComponentType, List[ComponentType]]
    ) -> responses.Destiny2.GetProfile:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.get(
            f'/{membership_type}/Profile/{membership_id}/',
            parameters=queries.Destiny2.GetProfile(components=components),
            response_format=responses.Destiny2.GetProfile
        )

    @endpoint(
        path='/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/',
        name='Destiny2.GetCharacter',
        description='Returns character information for the supplied character.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetCharacter.html'
            '#operation_get_Destiny2-GetCharacter'
        ),
        method='GET'
    )
    def get_character(
            self,
            membership_id: int,
            membership_type: MemberType,
            character_id: int,
            components: Union[ComponentType, List[ComponentType]]
    ) -> responses.Destiny2.GetCharacter:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.get(
            f'/{membership_type}/Profile/{membership_id}/Character/{character_id}/',
            parameters=queries.Destiny2.GetCharacter(components=components),
            response_format=responses.Destiny2.GetCharacter
        )

    @endpoint(
        path='/Destiny2/Clan/{groupId}/WeeklyRewardState/',
        name='Destiny2.GetClanWeeklyRewardState',
        description=(
            'Returns information on the weekly clan rewards and if the clan has earned them or not. Note that this '
            'will always report rewards as not redeemed.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetClanWeeklyRewardState.html'
            '#operation_get_Destiny2-GetClanWeeklyRewardState'
        ),
        method='GET'
    )
    def get_clan_weekly_reward_state(
            self,
            group_id: int
    ) -> responses.Destiny2.GetClanWeeklyRewardState:
        return self.get(
            f'/Clan/{group_id}/WeeklyRewardState/',
            response_format=responses.Destiny2.GetClanWeeklyRewardState
        )

    @endpoint(
        path='/Destiny2/Clan/ClanBannerDictionary/',
        name='Destiny2.GetClanBannerSource',
        description='Returns the dictionary of values for a Clan Banner.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetClanBannerSource.html'
            '#operation_get_Destiny2-GetClanBannerSource'
        ),
        method='GET'
    )
    def get_clan_banner_source(self) -> responses.Destiny2.GetClanBannerSource:
        return self.get(
            '/Clan/ClanBannerDictionary/',
            response_format=responses.Destiny2.GetClanBannerSource
        )

    @endpoint(
        path='/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Item/{itemInstanceId}/',
        name='Destiny2.GetItem',
        description=(
            'Retrieve the details of an instanced Destiny Item. An instanced Destiny item is one with an '
            'ItemInstanceId. Non-instanced items, such as materials, have no useful instance-specific details and thus '
            'are not queryable here.'
        ),
        href='https://bungie-net.github.io/multi/operation_get_Destiny2-GetItem.html#operation_get_Destiny2-GetItem',
        method='GET'
    )
    def get_item(
            self,
            membership_id: int,
            membership_type: MemberType,
            item_instance_id: int,
            components: Union[ComponentType, List[ComponentType]]
    ) -> responses.Destiny2.GetItem:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.get(
            f'/{membership_type}/Profile/{membership_id}/Item/{item_instance_id}/',
            parameters=queries.Destiny2.GetItem(components=components),
            response_format=responses.Destiny2.GetItem
        )

    @oauth_required(ApplicationScopes.ReadDestinyVendorsAndAdvisors)
    @endpoint(
        path='/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/',
        name='Destiny2.GetVendors',
        description=(
            'Get currently available vendors from the list of vendors that can possibly have rotating inventory. Note '
            'that this does not include things like preview vendors and vendors-as-kiosks, neither of whom have '
            'rotating/dynamic inventories. Use their definitions as-is for those.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetVendors.html'
            '#operation_get_Destiny2-GetVendors'
        ),
        method='GET'
    )
    def get_vendors(
            self,
            membership_id: int,
            membership_type: MemberType,
            character_id: int,
            components: Union[ComponentType, List[ComponentType]],
            vendor_filter: VendorFilter = Destiny.DestinyVendorFilter.None_
    ) -> responses.Destiny2.GetVendors:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.get(
            f'{membership_type}/Profile/{membership_id}/Character/{character_id}/Vendors/',
            parameters=queries.Destiny2.GetVendors(
                components=components,
                filter=vendor_filter,
            ),
            response_format=responses.Destiny2.GetVendors
        )

    @oauth_required(ApplicationScopes.ReadDestinyVendorsAndAdvisors)
    @endpoint(
        path='/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/',
        name='Destiny2.GetVendor',
        description='Get the details of a specific vendor.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetVendor.html#operation_get_Destiny2-GetVendor'
        ),
        method='GET'
    )
    def get_vendor(
            self,
            membership_id: int,
            membership_type: MemberType,
            character_id: int,
            vendor_hash: int,
            components: Union[ComponentType, List[ComponentType]],
    ) -> responses.Destiny2.GetVendor:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.get(
            f'/{membership_type}/Profile/{membership_id}/Character/{character_id}/Vendors/{vendor_hash}/',
            parameters=queries.Destiny2.GetVendor(components=components),
            response_format=responses.Destiny2.GetVendor
        )

    @endpoint(
        path='/Destiny2/Vendors/',
        name='Destiny2.GetPublicVendors [PREVIEW]',
        description=(
            'Get items available from vendors where the vendors have items for sale that are common for everyone. If '
            'any portion of the Vendor\'s available inventory is character or account specific, we will be unable to '
            'return their data from this endpoint due to the way that available inventory is computed. As I am often '
            'guilty of saying: \'It\'s a long story...\''
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetPublicVendors.html'
            '#operation_get_Destiny2-GetPublicVendors'
        ),
        method='GET'
    )
    def get_public_vendors(
            self,
            components: Union[ComponentType, List[ComponentType]]
    ) -> responses.Destiny2.GetPublicVendors:
        return self.get(
            '/Vendors/',
            parameters=queries.Destiny2.GetPublicVendors(components=components),
            response_format=responses.Destiny2.GetPublicVendors
        )

    @endpoint(
        path=(
                '/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Collectibles/'
                '{collectiblePresentationNodeHash}/'
        ),
        name='Destiny2.GetCollectibleNodeDetails',
        description=(
            'Given a Presentation Node that has Collectibles as direct descendants, this will return item details '
            'about those descendants in the context of the requesting character.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetCollectibleNodeDetails.html'
            '#operation_get_Destiny2-GetCollectibleNodeDetails'
        ),
        method='GET'
    )
    def get_collectible_node_details(
            self,
            membership_id: int,
            membership_type: MemberType,
            character_id: int,
            collection_presentation_node_hash: int,
            components: Union[ComponentType, List[ComponentType]],
    ) -> responses.Destiny2.GetCollectibleNodeDetails:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.get(
            f'/{membership_type}/Profile/{membership_id}/Character/{character_id}/Collectibles/'
            f'{collection_presentation_node_hash}/',
            parameters=queries.Destiny2.GetCollectibleNodeDetails(components=components),
            response_format=responses.Destiny2.GetCollectibleNodeDetails
        )

    @oauth_required(ApplicationScopes.MoveEquipDestinyItems)
    @endpoint(
        path='/Destiny2/Actions/Items/TransferItem/',
        name='Destiny2.TransferItem',
        description=(
            'Transfer an item to/from your vault. You must have a valid Destiny account. You must also pass BOTH a '
            'reference AND an instance ID if it\'s an instanced item.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Destiny2-TransferItem.html'
            '#operation_post_Destiny2-TransferItem'
        ),
        method='POST'
    )
    def transfer_item(
            self,
            item_hash: int,
            item_instance_id: int,
            character_id: int,
            membership_type: MemberType,
            is_item_in_vault: bool,
            stack_size: Optional[int] = None
    ) -> responses.Destiny2.TransferItem:
        return self.post(
            '/Actions/Items/TransferItem/',
            body=Destiny.Requests.DestinyItemTransferRequest(
                itemReferenceHash=item_hash,
                itemId=item_instance_id,
                characterId=character_id,
                membershipType=membership_type,
                transferToVault=not is_item_in_vault,
                stackSize=stack_size
            ),
            response_format=responses.Destiny2.TransferItem
        )

    @oauth_required(ApplicationScopes.MoveEquipDestinyItems)
    @endpoint(
        path='/Destiny2/Actions/Items/PullFromPostmaster/',
        name='Destiny2.PullFromPostmaster',
        description=(
            'Extract an item from the Postmaster, with whatever implications that may entail. You must have a valid '
            'Destiny account. You must also pass BOTH a reference AND an instance ID if it\'s an instanced item.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Destiny2-PullFromPostmaster.html'
            '#operation_post_Destiny2-PullFromPostmaster'
        ),
        method='POST'
    )
    def pull_from_postmaster(
            self,
            item_hash: int,
            item_instance_id: int,
            character_id: int,
            membership_type: MemberType,
            stack_size: Optional[int] = None
    ) -> responses.Destiny2.PullFromPostmaster:
        return self.post(
            '/Actions/Items/PullFromPostmaster/',
            body=Destiny.Requests.Actions.DestinyPostmasterTransferRequest(
                itemReferenceHash=item_hash,
                itemId=item_instance_id,
                characterId=character_id,
                membershipType=membership_type,
                stackSize=stack_size
            ),
            response_format=responses.Destiny2.PullFromPostmaster
        )

    @oauth_required(ApplicationScopes.MoveEquipDestinyItems)
    @endpoint(
        path='/Destiny2/Actions/Items/EquipItem/',
        name='Destiny2.EquipItem',
        description=(
                'Equip an item. You must have a valid Destiny Account, and either be in a social space, in orbit, or '
                'offline.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Destiny2-EquipItem.html'
            '#operation_post_Destiny2-EquipItem'
        ),
        method='POST'
    )
    def equip_item(
            self,
            item_instance_id: int,
            character_id: int,
            membership_type: MemberType
    ) -> responses.Destiny2.EquipItem:
        return self.post(
            '/Actions/Items/EquipItem/',
            body=Destiny.Requests.Actions.DestinyItemActionRequest(
                itemId=item_instance_id,
                characterId=character_id,
                membershipType=membership_type,
            ),
            response_format=responses.Destiny2.EquipItem
        )

    @oauth_required(ApplicationScopes.MoveEquipDestinyItems)
    @endpoint(
        path='/Destiny2/Actions/Items/EquipItems/',
        name='Destiny2.EquipItems',
        description=(
            'Equip a list of items by itemInstanceIds. You must have a valid Destiny Account, and either be in a '
            'social space, in orbit, or offline. Any items not found on your character will be ignored.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Destiny2-EquipItems.html'
            '#operation_post_Destiny2-EquipItems'
        ),
        method='POST'
    )
    def equip_items(
            self,
            item_instance_ids: List[int],
            character_id: int,
            membership_type: MemberType
    ) -> responses.Destiny2.EquipItems:
        return self.post(
            '/Actions/Items/EquipItems/',
            body=Destiny.Requests.Actions.DestinyItemSetActionRequest(
                itemIds=item_instance_ids,
                characterId=character_id,
                membershipType=membership_type
            ),
            response_format=responses.Destiny2.EquipItems
        )

    @oauth_required(ApplicationScopes.MoveEquipDestinyItems)
    @endpoint(
        path='/Destiny2/Actions/Items/SetLockState/',
        name='Destiny2.SetItemLockState',
        description='Set the Lock State for an instanced item. You must have a valid Destiny Account.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_Destiny2-SetItemLockState.html'
            '#operation_post_Destiny2-SetItemLockState'
        ),
        method='POST'
    )
    def set_item_lock_state(
            self,
            state: bool,
            item_instance_id: int,
            character_id: int,
            membership_type: MemberType
    ) -> responses.Destiny2.SetItemLockState:
        return self.post(
            '/Actions/Items/SetLockState/',
            body=Destiny.Requests.Actions.DestinyItemStateRequest(
                state=state,
                itemId=item_instance_id,
                characterId=character_id,
                membershipType=membership_type
            ),
            response_format=responses.Destiny2.SetItemLockState
        )

    @oauth_required(ApplicationScopes.MoveEquipDestinyItems)
    @endpoint(
        path='/Destiny2/Actions/Items/SetTrackedState/',
        name='Destiny2.SetQuestTrackedState',
        description=(
            'Set the Tracking State for an instanced item, if that item is a Quest or Bounty. You must have a valid '
            'Destiny Account. Yeah, it\'s an item.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Destiny2-SetQuestTrackedState.html'
            '#operation_post_Destiny2-SetQuestTrackedState'
        ),
        method='POST'
    )
    def set_quest_tracked_state(
            self,
            state: bool,
            item_instance_id: int,
            character_id: int,
            membership_type: MemberType
    ) -> responses.Destiny2.SetQuestTrackedState:
        return self.post(
            '/Actions/Items/SetTrackedState/',
            body=Destiny.Requests.Actions.DestinyItemStateRequest(
                state=state,
                itemId=item_instance_id,
                characterId=character_id,
                membershipType=membership_type
            ),
            response_format=responses.Destiny2.SetQuestTrackedState
        )

    @oauth_required(ApplicationScopes.AdvancedWriteActions)
    @endpoint(
        path='/Destiny2/Actions/Items/InsertSocketPlug/',
        name='Destiny2.InsertSocketPlug [PREVIEW]',
        description=(
            'Insert a plug into a socketed item. I know how it sounds, but I assure you it\'s much more G-rated than '
            'you might be guessing. We haven\'t decided yet whether this will be able to insert plugs that have side '
            'effects, but if we do it will require special scope permission for an application attempting to do so. '
            'You must have a valid Destiny Account, and either be in a social space, in orbit, or offline. Request '
            'must include proof of permission for \'InsertPlugs\' from the account owner.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Destiny2-InsertSocketPlug.html'
            '#operation_post_Destiny2-InsertSocketPlug'
        ),
        method='POST'
    )
    def insert_socket_plug(
            self,
            item_instance_id: int,
            socket_index: int,
            socket_array_type: SocketArrayType,
            plug_item_hash: int,
            action_token: str,
            character_id: int,
            membership_type: MemberType
    ) -> responses.Destiny2.InsertSocketPlug:
        return self.post(
            '/Actions/Items/InsertSocketPlug/',
            body=Destiny.Requests.Actions.DestinyInsertPlugsActionRequest(
                actionToken=action_token,
                itemInstanceId=item_instance_id,
                plug=Destiny.Requests.Actions.DestinyInsertPlugsRequestEntry(
                    socketIndex=socket_index,
                    socketArrayType=socket_array_type,
                    plugItemHash=plug_item_hash
                ),
                characterId=character_id,
                membershipType=membership_type
            ),
            response_format=responses.Destiny2.InsertSocketPlug
        )

    @oauth_required(ApplicationScopes.MoveEquipDestinyItems)
    @endpoint(
        path='/Destiny2/Actions/Items/InsertSocketPlugFree/',
        name='Destiny2.InsertSocketPlugFree [PREVIEW]',
        description=(
            'Insert a \'free\' plug into an item\'s socket. This does not require \'Advanced Write Action\' '
            'authorization and is available to 3rd-party apps, but will only work on \'free and reversible\' socket '
            'actions (Perks, Armor Mods, Shaders, Ornaments, etc.). You must have a valid Destiny Account, and the '
            'character must either be in a social space, in orbit, or offline.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Destiny2-InsertSocketPlugFree.htm'
            '#operation_post_Destiny2-InsertSocketPlugFree'
        ),
        method='POST'
    )
    def insert_socket_plug_free(
            self,
            item_instance_id: int,
            socket_index: int,
            socket_array_type: SocketArrayType,
            plug_item_hash: int,
            character_id: int,
            membership_type: MemberType
    ) -> responses.Destiny2.InsertSocketPlugFree:
        return self.post(
            '/Actions/Items/InsertSocketPlugFree/',
            body=Destiny.Requests.Actions.DestinyInsertPlugsFreeActionRequest(
                plug=Destiny.Requests.Actions.DestinyInsertPlugsRequestEntry(
                    socketIndex=socket_index,
                    socketArrayType=socket_array_type,
                    plugItemHash=plug_item_hash
                ),
                itemId=item_instance_id,
                characterId=character_id,
                membershipType=membership_type
            ),
            response_format=responses.Destiny2.InsertSocketPlugFree
        )

    @endpoint(
        path='/Destiny2/Stats/PostGameCarnageReport/{activityId}/',
        name='Destiny2.GetPostGameCarnageReport',
        description='Gets the available post game carnage report for the activity ID.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetPostGameCarnageReport.html'
            '#operation_get_Destiny2-GetPostGameCarnageReport'
        ),
        method='GET'
    )
    def get_post_game_carnage_report(
            self,
            activity_instance_id: int
    ) -> responses.Destiny2.GetPostGameCarnageReport:
        return self.get(
            f'/Stats/PostGameCarnageReport/{activity_instance_id}/',
            response_format=responses.Destiny2.GetPostGameCarnageReport
        )

    @oauth_required(ApplicationScopes.BnetWrite)
    @endpoint(
        path='/Destiny2/Stats/PostGameCarnageReport/{activityId}/Report/',
        name='Destiny2.ReportOffensivePostGameCarnageReportPlayer',
        description=(
            'Report a player that you met in an activity that was engaging in ToS-violating activities. Both you and '
            'the offending player must have played in the activityId passed in. Please use this judiciously and only '
            'when you have strong suspicions of violation, pretty please.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Destiny2-ReportOffensivePostGameCarnageReportPlayer.html'
            '#operation_post_Destiny2-ReportOffensivePostGameCarnageReportPlayer'
        ),
        method='POST'
    )
    def report_offensive_post_game_carnage_report_player(
            self,
            activity_instance_id: int,
            reason_category_hashes: List[int],
            reason_hashes: Optional[List[int]],
            offending_character_id: int
    ) -> responses.Destiny2.ReportOffensivePostGameCarnageReportPlayer:
        return self.post(
            f'/Stats/PostGameCarnageReport/{activity_instance_id}/Report/',
            body=Destiny.Reporting.Requests.DestinyReportOffensePgcrRequest(
                reasonCategoryHashes=reason_category_hashes,
                reasonHashes=reason_hashes,
                offendingCharacterId=offending_character_id
            ),
            response_format=responses.Destiny2.ReportOffensivePostGameCarnageReportPlayer
        )

    @endpoint(
        path='/Destiny2/Stats/Definition/',
        name='Destiny2.GetHistoricalStatsDefinition',
        description='Gets historical stats definitions.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetHistoricalStatsDefinition.html'
            '#operation_get_Destiny2-GetHistoricalStatsDefinition'
        ),
        method='GET'
    )
    def get_historical_stats_definition(self) -> responses.Destiny2.GetHistoricalStatsDefinition:
        return self.get(
            '/Stats/Definition/',
            response_format=responses.Destiny2.GetHistoricalStatsDefinition
        )

    @endpoint(
        path='/Destiny2/Stats/Leaderboards/Clans/{groupId}/',
        name='Destiny2.GetClanLeaderboards [PREVIEW]',
        description=(
            'Gets leaderboards with the signed in user\'s friends and the supplied destinyMembershipId as the focus. '
            'PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but '
            'there may be bugs that prevent desirable operation.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetClanLeaderboards.html'
            '#operation_get_Destiny2-GetClanLeaderboards'
        ),
        method='GET'
    )
    def get_clan_leaderboards(
            self,
            clan_id: int,
            num: Optional[int] = None,
            modes: Union[
                ActivityModeType, List[ActivityModeType]
            ] = Destiny.HistoricalStats.Definitions.DestinyActivityModeType.None_,
            stat_id: Optional[str] = None
    ) -> responses.Destiny2.GetClanLeaderboards:
        return self.get(
            f'/Stats/Leaderboards/Clans/{clan_id}/',
            parameters=queries.Destiny2.GetClanLeaderboards(
                maxtop=num,
                modes=modes,
                statid=stat_id
            ),
            response_format=responses.Destiny2.GetClanLeaderboards
        )

    @endpoint(
        path='/Destiny2/Stats/AggregateClanStats/{groupId}/',
        name='Destiny2.GetClanAggregateStats [PREVIEW]',
        description=(
            'Gets aggregated stats for a clan using the same categories as the clan leaderboards. PREVIEW: This '
            'endpoint is still in beta, and may experience rough edges. The schema is in final form, but there may be '
            'bugs that prevent desirable operation.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetClanAggregateStats.html'
            '#operation_get_Destiny2-GetClanAggregateStats'
        ),
        method='GET'
    )
    def get_clan_aggregate_stats(
            self,
            clan_id: int,
            modes: Union[
                ActivityModeType, List[ActivityModeType]
            ] = Destiny.HistoricalStats.Definitions.DestinyActivityModeType.None_
    ) -> responses.Destiny2.GetClanAggregateStats:
        return self.get(
            f'/Stats/AggregateClanStats/{clan_id}/',
            parameters=queries.Destiny2.GetClanAggregateStats(modes=modes),
            response_format=responses.Destiny2.GetClanAggregateStats
        )

    @endpoint(
        path='/Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/',
        name='Destiny2.GetLeaderboards [PREVIEW]',
        description=(
            'Gets leaderboards with the signed in user\'s friends and the supplied destinyMembershipId as the focus. '
            'PREVIEW: This endpoint has not yet been implemented. It is being returned for a preview of future '
            'functionality, and for public comment/suggestion/preparation.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetLeaderboards.html'
            '#operation_get_Destiny2-GetLeaderboards'
        ),
        method='GET'
    )
    def get_leaderboards(self):
        raise NotImplementedError(
            f'The "{self.get_leaderboards_for_character.__endpoint_name__}" endpoint does not yet exist, it is only available as an example for a future endpoint.'
        )

    @endpoint(
        path='/Destiny2/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/',
        name='Destiny2.GetLeaderboardsForCharacter [PREVIEW]',
        description=(
            'Gets leaderboards with the signed in user\'s friends and the supplied destinyMembershipId as the focus. '
            'PREVIEW: This endpoint is still in beta, and may experience rough edges. The schema is in final form, but '
            'there may be bugs that prevent desirable operation.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetLeaderboardsForCharacter.html'
            '#operation_get_Destiny2-GetLeaderboardsForCharacter'
        ),
        method='GET'
    )
    def get_leaderboards_for_character(self):
        raise NotImplementedError(
            f'The "{self.get_leaderboards_for_character.__endpoint_name__}" endpoint does not yet exist, it is only available as an example for a future endpoint.'
        )

    @endpoint(
        path='/Destiny2/Armory/Search/{type}/{searchTerm}/',
        name='Destiny2.SearchDestinyEntities',
        description='Gets a page list of Destiny items.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-SearchDestinyEntities.html'
            '#operation_get_Destiny2-SearchDestinyEntities'
        ),
        method='GET'
    )
    def search_destiny_entities(
            self,
            entity_type: str,
            search_term: str,
            page: Optional[int] = None
    ) -> responses.Destiny2.SearchDestinyEntities:
        return self.get(
            f'/Armory/Search/{entity_type}/{search_term}/',
            parameters=queries.Destiny2.SearchDestinyEntities(page=page),
            response_format=responses.Destiny2.SearchDestinyEntities
        )

    @endpoint(
        path='/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/',
        name='Destiny2.GetHistoricalStats',
        description='Get historical stats for the indicated character.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetHistoricalStats.html'
            '#operation_get_Destiny2-GetHistoricalStats'
        ),
        method='GET'
    )
    def get_historical_stats(
            self,
            membership_id: int,
            membership_type: MemberType,
            character_id: int,
            groups: Optional[
                Union[StatsGroupType, List[StatsGroupType]]
            ] = Destiny.HistoricalStats.Definitions.DestinyStatsGroupType.None_,
            modes: Union[
                ActivityModeType, List[ActivityModeType]
            ] = Destiny.HistoricalStats.Definitions.DestinyActivityModeType.None_,
            period_type: Optional[PeriodType] = Destiny.HistoricalStats.Definitions.PeriodType.None_,
            period_start: Union[str, 'datetime'] = None,
            period_end: Union[str, 'datetime'] = None,
    ) -> responses.Destiny2.GetHistoricalStats:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.get(
            f'/{membership_type}/Account/{membership_id}/Character/{character_id}/Stats/',
            parameters=queries.Destiny2.GetHistoricalStats(
                dayend=period_end,
                daystart=period_start,
                groups=groups,
                modes=modes,
                periodType=period_type
            ),
            response_format=responses.Destiny2.GetHistoricalStats
        )

    @endpoint(
        path='/Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/',
        name='Destiny2.GetHistoricalStatsForAccount',
        description='Gets aggregated historical stats organized around each character for a given account.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetHistoricalStatsForAccount.html'
            '#operation_get_Destiny2-GetHistoricalStatsForAccount'
        ),
        method='GET'
    )
    def get_historical_stats_for_account(
            self,
            membership_id: int,
            membership_type: MemberType,
            groups: Optional[
                Union[StatsGroupType, List[StatsGroupType]]
            ] = Destiny.HistoricalStats.Definitions.DestinyStatsGroupType.None_
    ) -> responses.Destiny2.GetHistoricalStatsForAccount:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.get(
            f'/{membership_type}/Account/{membership_id}/Stats/',
            parameters=queries.Destiny2.GetHistoricalStatsForAccount(groups=groups),
            response_format=responses.Destiny2.GetHistoricalStatsForAccount
        )

    @endpoint(
        path='/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/',
        name='Destiny2.GetActivityHistory',
        description='Gets activity history stats for indicated characters.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetActivityHistory.html'
            '#operation_get_Destiny2-GetActivityHistory'
        ),
        method='GET'
    )
    def get_activity_history(
            self,
            membership_id: int,
            membership_type: MemberType,
            character_id: int,
            count: Optional[int] = None,
            mode: Optional[ActivityModeType] = Destiny.HistoricalStats.Definitions.DestinyActivityModeType.None_,
            page: Optional[int] = None,
    ) -> responses.Destiny2.GetActivityHistory:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.get(
            f'/{membership_type}/Account/{membership_id}/Character/{character_id}/Stats/Activities/',
            parameters=queries.Destiny2.GetActivityHistory(
                count=count,
                mode=mode,
                page=page
            ),
            response_format=responses.Destiny2.GetActivityHistory
        )

    @endpoint(
        path='/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/UniqueWeapons/',
        name='Destiny2.GetUniqueWeaponHistory',
        description='Gets details about unique weapon usage, including all exotic weapons.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetUniqueWeaponHistory.html'
            '#operation_get_Destiny2-GetUniqueWeaponHistory'
        ),
        method='GET'
    )
    def get_unique_weapon_history(
            self,
            membership_id: int,
            membership_type: MemberType,
            character_id: int,
    ) -> responses.Destiny2.GetUniqueWeaponHistory:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.get(
            f'/{membership_type}/Account/{membership_id}/Character/{character_id}/Stats/UniqueWeapons/',
            response_format=responses.Destiny2.GetUniqueWeaponHistory
        )

    @endpoint(
        path=(
                '/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats'
                '/AggregateActivityStats/'
        ),
        name='Destiny2.GetDestinyAggregateActivityStats',
        description=(
                'Gets all activities the character has participated in together with aggregate statistics for those '
                'activities.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetDestinyAggregateActivityStats.html'
            '#operation_get_Destiny2-GetDestinyAggregateActivityStats'
        ),
        method='GET'
    )
    def get_destiny_aggregate_activity_stats(
            self,
            membership_id: int,
            membership_type: MemberType,
            character_id: int
    ) -> responses.Destiny2.GetDestinyAggregateActivityStats:
        membership_type = BungieMembershipType.int_validator(membership_type)

        return self.get(
            f'/{membership_type}/Account/{membership_id}/Character/{character_id}/Stats/AggregateActivityStats/',
            response_format=responses.Destiny2.GetDestinyAggregateActivityStats
        )

    @endpoint(
        path='/Destiny2/Milestones/{milestoneHash}/Content/',
        name='Destiny2.GetPublicMilestoneContent',
        description='Gets custom localized content for the milestone of the given hash, if it exists.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetPublicMilestoneContent.html'
            '#operation_get_Destiny2-GetPublicMilestoneContent'
        ),
        method='GET'
    )
    def get_public_milestone_content(self, milestone_hash: int) -> responses.Destiny2.GetPublicMilestoneContent:
        return self.get(
            f'/Milestones/{milestone_hash}/Content/',
            response_format=responses.Destiny2.GetPublicMilestoneContent
        )

    @endpoint(
        path='/Destiny2/Milestones/',
        name='Destiny2.GetPublicMilestones',
        description='Gets public information about currently available milestones.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-GetPublicMilestones.html'
            '#operation_get_Destiny2-GetPublicMilestones'
        ),
        method='GET'
    )
    def get_public_milestones(self) -> responses.Destiny2.GetPublicMilestones:
        return self.get(
            '/Milestones/',
            response_format=responses.Destiny2.GetPublicMilestones
        )

    @oauth_required(ApplicationScopes.AdvancedWriteActions)
    @endpoint(
        path='/Destiny2/Awa/Initialize/',
        name='Destiny2.AwaInitializeRequest',
        description='Initialize a request to perform an advanced write action.'
    )
    def awa_initialize_request(
            self,
            awa_type: AwaType,
            membership_type: MemberType,
            character_id: Optional[int] = None,
            affected_item_id: Optional[int] = None,
    ) -> responses.Destiny2.AwaInitializeRequest:
        return self.post(
            '/Awa/Initialize/',
            body=Destiny.Advanced.AwaPermissionRequested(
                type=awa_type,
                affectedItemId=affected_item_id,
                membershipType=membership_type,
                characterId=character_id
            ),
            response_format=responses.Destiny2.AwaInitializeRequest
        )

    @endpoint(
        path='/Destiny2/Awa/AwaProvideAuthorizationResult/',
        name='Destiny2.AwaProvideAuthorizationResult',
        description=(
                'Provide the result of the user interaction. Called by the Bungie Destiny App to approve or reject a '
                'request.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_Destiny2-AwaProvideAuthorizationResult.html'
            '#operation_post_Destiny2-AwaProvideAuthorizationResult'
        ),
        method='POST'
    )
    def awa_provide_authorization_result(
            self,
            selection: int,
            correlation_id: str,
            nonce: List[str]
    ) -> responses.Destiny2.AwaProvideAuthorizationResult:
        return self.post(
            '/Awa/AwaProvideAuthorizationResult/',
            body=Destiny.Advanced.AwaUserResponse(
                selection=selection,
                correlationId=correlation_id,
                nonce=nonce
            ),
            response_format=responses.Destiny2.AwaProvideAuthorizationResult
        )

    @oauth_required(ApplicationScopes.AdvancedWriteActions)
    @endpoint(
        path='/Destiny2/Awa/GetActionToken/{correlationId}/',
        name='Destiny2.AwaGetActionToken',
        description='Returns the action token if user approves the request.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Destiny2-AwaGetActionToken.html'
            '#operation_get_Destiny2-AwaGetActionToken'
        ),
        method='GET'
    )
    def awa_get_action_token(
            self,
            correlation_id: str
    ) -> responses.Destiny2.AwaGetActionToken:
        return self.get(
            f'/Awa/GetActionToken/{correlation_id}/',
            response_format=responses.Destiny2.AwaGetActionToken
        )


def setup(client: Union[SyncClient, AsyncClient]) -> None:
    client.add_subclient(Destiny2())
