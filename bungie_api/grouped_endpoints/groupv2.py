from typing import Union, Optional, Dict, List

from arya_api_framework import SyncClient, AsyncClient, SubClient
from arya_api_framework.utils import apiclient, endpoint

from ..decorators import destinyclient, oauth_required
from ..models import responses, queries
from ..models.entities.Applications import ApplicationScopes
from ..models.entities.User import UserMembership
from ..models.entities import BungieMembershipType
from ..models.entities.GroupsV2 import (
    GroupType,
    GroupSortBy,
    GroupMemberCountFilter,
    GroupDateRange,
    MembershipOption,
    ChatSecuritySetting,
    GroupHomepage,
    GroupPostPublicity,
    ClanBanner,
    HostGuidedGamesPermissionLevel,
    RuntimeGroupMemberType,
    GroupsForMemberFilter
)


__all__ = [
    'GroupV2',
]


@destinyclient
@apiclient
class GroupV2(SubClient, name='groupv2', relative_path='GroupV2'):
    @endpoint(
        path='/GroupV2/GetAvailableAvatars/',
        name='GroupV2.GetAvailableAvatars',
        description='Returns a list of all available group avatars for the signed-in user.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_GroupV2-GetAvailableAvatars.html'
            '#operation_get_GroupV2-GetAvailableAvatars'
        ),
        method='GET'
    )
    def get_available_avatars(self) -> responses.GroupV2.GetAvailableAvatars:
        return self.get(
            '/GetAvailableAvatars/',
            response_format=responses.GroupV2.GetAvailableAvatars
        )

    @endpoint(
        path='/GroupV2/GetAvailableThemes/',
        name='GroupV2.GetAvailableThemes',
        description='Returns a list of all available group themes.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_GroupV2-GetAvailableThemes.html'
            '#operation_get_GroupV2-GetAvailableThemes'
        ),
        method='GET'
    )
    def get_available_themes(self) -> responses.GroupV2.GetAvailableThemes:
        return self.get(
            '/GetAvailableThemes/',
            response_format=responses.GroupV2.GetAvailableThemes
        )

    @oauth_required(ApplicationScopes.ReadUserData)
    @endpoint(
        path='/GroupV2/GetUserClanInviteSetting/{mType}/',
        name='GroupV2.GetUserClanInviteSetting',
        description=(
            'Gets the state of the user\'s clan invite preferences for a particular membership type - '
            'true if they wish to be invited to clans, false for otherwise.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_GroupV2-GetUserClanInviteSetting.html'
            '#operation_get_GroupV2-GetUserClanInviteSetting'
        ),
        method='GET'
    )
    def get_user_clan_invite_setting(
            self,
            membership_type: Union[int, BungieMembershipType]
    ) -> responses.GroupV2.GetUserClanInviteSetting:
        if not isinstance(membership_type, BungieMembershipType):
            membership_type = BungieMembershipType(membership_type)

        return self.get(
            f'/GetUserClanInviteSetting/{membership_type.value}/',
            response_format=responses.GroupV2.GetUserClanInviteSetting
        )

    @oauth_required(ApplicationScopes.ReadGroups)
    @endpoint(
        path='/GroupV2/Recommended/{groupType}/{createDateRange}/',
        name='GroupV2.GetRecommendedGroups',
        description='Gets groups recommended for you based on the groups to whom those you follow belong.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-GetRecommendedGroups.html'
            '#operation_post_GroupV2-GetRecommendedGroups'
        ),
        method='POST'
    )
    def get_recommended_groups(
            self,
            group_type: Union[int, GroupType] = GroupType.General,
            date_range: int = 0,
    ) -> responses.GroupV2.GetRecommendedGroups:
        if not isinstance(group_type, GroupType):
            group_type = GroupType(group_type)

        return self.post(
            f'/Recommended/{group_type.value}/{date_range}/',
            response_format=responses.GroupV2.GetRecommendedGroups
        )

    @endpoint(
        path='/GroupV2/Search/',
        name='GroupV2.GroupSearch',
        description='Search for groups.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-GroupSearch.html'
            '#operation_post_GroupV2-GroupSearch'
        ),
        method='POST'
    )
    def group_search(
            self,
            name: Optional[str] = None,
            group_type: Optional[Union[int, GroupType]] = None,
            creation_date: Optional[Union[int, GroupDateRange]] = None,
            sort_by: Optional[Union[int, GroupSortBy]] = None,
            group_member_count_filter: Optional[Union[int, GroupMemberCountFilter]] = None,
            locale_filter: Optional[str] = None,
            tag_text: Optional[str] = None,
            items_per_page: Optional[int] = None,
            page: Optional[int] = None,
            request_continuation_token: Optional[str] = None,
    ) -> responses.GroupV2.GroupSearch:
        return self.post(
            '/Search/',
            body=queries.GroupsV2.GroupQuery(
                name=name,
                groupType=group_type,
                creationDate=creation_date,
                sortBy=sort_by,
                groupMemberCountFilter=group_member_count_filter,
                localeFilter=locale_filter,
                tagText=tag_text,
                itemsPerPage=items_per_page,
                currentPage=page,
                requestContinuationToken=request_continuation_token
            ),
            response_format=responses.GroupV2.GroupSearch
        )

    @endpoint(
        path='/GroupV2/{groupId}/',
        name='GroupV2.GetGroup',
        description='Get information about a specific group via its id.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_GroupV2-GetGroup.html'
            '#operation_get_GroupV2-GetGroup'
        ),
        method='GET'
    )
    def get_group(self, group_id: int) -> responses.GroupV2.GetGroup:
        return self.get(
            f'/{group_id}/',
            response_format=responses.GroupV2.GetGroup
        )

    @endpoint(
        path='/GroupV2/Name/{groupName}/{groupType}/',
        name='GroupV2.GetGroupByName',
        description='Get information about a specific group with the given name and type.',
        href=(
            'https://bungie-net.github.io/multi/schema_Forum-PostSearchResponse.html'
            '#schema_Forum-PostSearchResponse'
        ),
        method='GET'
    )
    def get_group_by_name(
            self,
            group_name: str,
            group_type: Union[int, GroupType] = GroupType.General
    ) -> responses.GroupV2.GetGroupByName:
        if not isinstance(group_type, GroupType):
            group_type = GroupType(group_type)

        return self.get(
            f'/Name/{group_name}/{group_type.value}/',
            response_format=responses.GroupV2.GetGroupByName
        )

    @endpoint(
        path='/GroupV2/NameV2/',
        name='GroupV2.GetGroupByNameV2',
        description='Get information about a specific group with the given name and type. The POST version.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-GetGroupByNameV2.html'
            '#operation_post_GroupV2-GetGroupByNameV2'
        ),
        method='POST'
    )
    def get_group_by_name_v2(
            self,
            group_name: str,
            group_type: Union[int, GroupType] = GroupType.General
    ) -> responses.GroupV2.GetGroupByNameV2:
        return self.post(
            '/NameV2/',
            body=queries.GroupsV2.GroupNameSearchRequest(
                groupName=group_name,
                groupType=group_type
            ),
            response_format=responses.GroupV2.GetGroupByNameV2
        )

    @endpoint(
        path='/GroupV2/{groupId}/OptionalConversations/',
        name='GroupV2.GetGroupOptionalConversations',
        description='Gets a list of available optional conversation channels and their settings.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_GroupV2-GetGroupOptionalConversations.html'
            '#operation_get_GroupV2-GetGroupOptionalConversations'
        ),
        method='GET'
    )
    def get_group_optional_conversations(
            self,
            group_id: int
    ) -> responses.GroupV2.GetGroupOptionalConversations:
        return self.get(
            f'/{group_id}/OptionalConversations/',
            response_format=responses.GroupV2.GetGroupOptionalConversations
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Edit/',
        name='GroupV2.EditGroup',
        description=(
            'Edit an existing group. You must have suitable permissions in the group to perform this operation. This '
            'latest revision will only edit the fields you pass in - pass null for properties you want to leave '
            'unaltered.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-EditGroup.html#operation_post_GroupV2-EditGroup'
        ),
        method='POST'
    )
    def edit_group(
            self,
            group_id: int,
            name: Optional[str] = None,
            about: Optional[str] = None,
            motto: Optional[str] = None,
            theme: Optional[str] = None,
            avatar_image_index: Optional[int] = None,
            tags: Optional[str] = None,
            is_public: Optional[bool] = None,
            membership_option: Optional[Union[int, MembershipOption]] = None,
            is_public_topic_admin_only: Optional[bool] = None,
            allow_chat: Optional[bool] = None,
            chat_security: Optional[Union[int, ChatSecuritySetting]] = None,
            callsign: Optional[str] = None,
            locale: Optional[str] = None,
            homepage: Optional[Union[int, GroupHomepage]] = None,
            enable_invitation_messaging_for_admins: Optional[bool] = None,
            default_publicity: Optional[Union[int, GroupPostPublicity]] = None
    ) -> responses.GroupV2.EditGroup:
        return self.post(
            f'/{group_id}/Edit/',
            body=queries.GroupsV2.GroupEditAction(
                name=name,
                about=about,
                motto=motto,
                theme=theme,
                avatarImageIndex=avatar_image_index,
                tags=tags,
                isPublic=is_public,
                membershipOption=membership_option,
                isPublicTopicAdminOnly=is_public_topic_admin_only,
                allowChat=allow_chat,
                chatSecurity=chat_security,
                callsign=callsign,
                locale=locale,
                homepage=homepage,
                enableInvitationMessagingForAdmins=enable_invitation_messaging_for_admins,
                defaultPublicity=default_publicity
            ),
            response_format=responses.GroupV2.EditGroup
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/EditClanBanner/',
        name='GroupV2.EditClanBanner',
        description=(
                'Edit an existing group\'s clan banner. You must have suitable permissions in the group to perform '
                'this operation. All fields are required.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-EditClanBanner.html'
            '#operation_post_GroupV2-EditClanBanner'
        ),
        method='POST'
    )
    def edit_clan_banner(
            self,
            group_id: int,
            decal_id: int,
            decal_color_id: int,
            decal_background_color_id: int,
            gonfalon_id: int,
            gonfalon_color_id: int,
            gonfalon_detail_id: int,
            gonfalon_detail_color_id: int
    ) -> responses.GroupV2.EditClanBanner:
        return self.post(
            f'/{group_id}/EditClanBanner/',
            body=ClanBanner(
                decalId=decal_id,
                decalColorId=decal_color_id,
                decalBackgroundColorId=decal_background_color_id,
                gonfalonId=gonfalon_id,
                gonfalonColorId=gonfalon_color_id,
                gonfalonDetailId=gonfalon_detail_id,
                gonfalonDetailColorId=gonfalon_detail_color_id
            ),
            response_format=responses.GroupV2.EditClanBanner
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/EditFounderOptions/',
        name='GroupV2.EditFounderOptions',
        description=(
                'Edit group options only available to a founder. You must have suitable permissions in the group to '
                'perform this operation.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-EditFounderOptions.html'
            '#operation_post_GroupV2-EditFounderOptions'
        ),
        method='POST'
    )
    def edit_founder_options(
            self,
            group_id: int,
            invite_permission_override: Optional[bool] = None,
            update_culture_permission_override: Optional[bool] = None,
            host_guided_game_permission_override: Optional[Union[int, HostGuidedGamesPermissionLevel]] = None,
            update_banner_permission_override: Optional[bool] = None,
            join_level: Optional[Union[int, RuntimeGroupMemberType]] = None
    ) -> responses.GroupV2.EditFounderOptions:
        return self.post(
            f'/{group_id}/EditFounderOptions/',
            body=queries.GroupsV2.GroupOptionsEditAction(
                InvitePermissionOverride=invite_permission_override,
                UpdateCulturePermissionoverride=update_culture_permission_override,
                HostGuidedGamePermissionOverride=host_guided_game_permission_override,
                UpdateBannerPermissionOverride=update_banner_permission_override,
                JoinLevel=join_level
            ),
            response_format=responses.GroupV2.EditFounderOptions
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/OptionalConversations/Add/',
        name='GroupV2.AddOptionalConversation',
        description='Add a new optional conversation/chat channel. Requires admin permissions to the group.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-AddOptionalConversation.html'
            '#operation_post_GroupV2-AddOptionalConversation'
        ),
        method='POST'
    )
    def add_optional_conversation(
            self,
            group_id: int,
            chat_name: str,
            chat_security: Union[int, ChatSecuritySetting] = ChatSecuritySetting.Group
    ) -> responses.GroupV2.AddOptionalConversation:
        return self.post(
            f'/{group_id}/OptionalConversations/Add/',
            body=queries.GroupsV2.GroupOptionalConversationAddRequest(
                chatName=chat_name,
                chatSecurity=chat_security
            ),
            response_format=responses.GroupV2.AddOptionalConversation
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/OptionalConversations/Edit/{conversationId}/',
        name='GroupV2.EditOptionalConversation',
        description=(
                'Edit the settings of an optional conversation/chat channel. Requires admin permissions to the group.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-EditOptionalConversation.html'
            '#operation_post_GroupV2-EditOptionalConversation'
        ),
        method='POST'
    )
    def edit_optional_conversation(
            self,
            group_id: int,
            conversation_id: int,
            chat_enabled: Optional[bool] = None,
            chat_name: Optional[str] = None,
            chat_security: Optional[Union[int, ChatSecuritySetting]] = None
    ) -> responses.GroupV2.EditOptionalConversation:
        return self.post(
            f'/{group_id}/OptionalConversations/Edit/{conversation_id}/',
            body=queries.GroupsV2.GroupOptionalConversationEditRequest(
                chatEnabled=chat_enabled,
                chatName=chat_name,
                chatSecurity=chat_security
            ),
            response_format=responses.GroupV2.EditOptionalConversation
        )

    @endpoint(
        path='/GroupV2/{groupId}/Members/',
        name='GroupV2.GetMembersOfGroup',
        description='Get the list of members in a given group.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_GroupV2-GetMembersOfGroup.html'
            '#operation_get_GroupV2-GetMembersOfGroup'
        ),
        method='GET'
    )
    def get_members_of_group(
            self,
            group_id: int,
            page: Optional[int] = 1,
            member_type: Optional[Union[int, RuntimeGroupMemberType]] = RuntimeGroupMemberType.None_,
            name_search: Optional[str] = None,
    ) -> responses.GroupV2.GetMembersOfGroup:
        return self.get(
            f'/{group_id}/Members/',
            parameters=queries.GroupsV2.GetMembersOfGroup(
                currentpage=page,
                memberType=member_type,
                nameSearch=name_search
            ),
            response_format=responses.GroupV2.GetMembersOfGroup
        )

    @endpoint(
        path='/GroupV2/{groupId}/AdminsAndFounder/',
        name='GroupV2.GetAdminsAndFounderOfGroup',
        description='Get the list of members who are of admin level or higher.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_GroupV2-GetAdminsAndFounderOfGroup.html'
            '#operation_get_GroupV2-GetAdminsAndFounderOfGroup'
        ),
        method='GET'
    )
    def get_admins_and_founder_of_group(
            self,
            group_id: int,
            page: Optional[int] = 1
    ) -> responses.GroupV2.GetAdminsAndFounderOfGroup:
        return self.get(
            f'/{group_id}/AdminsAndFounder/',
            parameters=queries.GroupsV2.GetAdminsAndFounderOfGroup(currentpage=page),
            response_format=responses.GroupV2.GetAdminsAndFounderOfGroup
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Members/{membershipType}/{membershipId}/SetMembershipType/{memberType}/',
        name='GroupV2.EditGroupMembership',
        description=(
                'Edit the membership type of a given member. You must have suitable permissions in the group to '
                'perform this operation.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-EditGroupMembership.html'
            '#operation_post_GroupV2-EditGroupMembership'
        ),
        method='POST'
    )
    def edit_group_membership(
            self,
            group_id: int,
            membership_id: int,
            membership_type: Union[int, BungieMembershipType],
            member_type: Union[int, RuntimeGroupMemberType],
    ) -> responses.GroupV2.EditGroupMembership:
        if not isinstance(membership_type, BungieMembershipType):
            membership_type = BungieMembershipType(membership_type)
        if not isinstance(member_type, RuntimeGroupMemberType):
            member_type = RuntimeGroupMemberType(member_type)

        return self.post(
            f'/{group_id}/Members/{membership_type.value}/{membership_id}/SetMembershipType/{member_type.value}/',
            response_format=responses.GroupV2.EditGroupMembership
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Kick/',
        name='GroupV2.KickMember',
        description=(
            'Kick a member from the given group, forcing them to reapply if they wish to re-join the group. You must '
            'have suitable permissions in the group to perform this operation.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-KickMember.html'
            '#operation_post_GroupV2-KickMember'
        ),
        method='POST'
    )
    def kick_member(
            self,
            group_id: int,
            membership_id: int,
            membership_type: Union[int, BungieMembershipType]
    ) -> responses.GroupV2.KickMember:
        if not isinstance(membership_type, BungieMembershipType):
            membership_type = BungieMembershipType(membership_type)

        return self.post(
            f'/{group_id}/Members/{membership_type.value}/{membership_id}/Kick/',
            response_format=responses.GroupV2.KickMember
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Ban/',
        name='GroupV2.BanMember',
        description='Bans the requested member from the requested group for the specified period of time.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-BanMember.html#operation_post_GroupV2-BanMember'
        ),
        method='POST'
    )
    def ban_member(
            self,
            group_id: int,
            membership_id: int,
            membership_type: Union[int, BungieMembershipType],
            comment: Optional[str] = None,
            length: Optional[int] = None
    ) -> responses.GroupV2.BanMember:
        if not isinstance(membership_type, BungieMembershipType):
            membership_type = BungieMembershipType(membership_type)

        return self.post(
            f'/{group_id}/Members/{membership_type.value}/{membership_id}/Ban/',
            body=queries.GroupsV2.GroupBanRequest(
                comment=comment,
                length=length
            ),
            response_format=responses.GroupV2.BanMember
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Unban/',
        name='GroupV2.UnbanMember',
        description='Unbans the requested member, allowing them to re-apply for membership.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-UnbanMember.html'
            '#operation_post_GroupV2-UnbanMember'
        ),
        method='POST'
    )
    def unban_member(
            self,
            group_id: int,
            membership_id: int,
            membership_type: Union[int, BungieMembershipType]
    ) -> responses.GroupV2.UnbanMember:
        if not isinstance(membership_type, BungieMembershipType):
            membership_type = BungieMembershipType(membership_type)

        return self.post(
            f'/{group_id}/Members/{membership_type.value}/{membership_id}/Unban/',
            response_format=responses.GroupV2.UnbanMember
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Banned/',
        name='GroupV2.GetBannedMembersOfGroup',
        description=(
            'Get the list of banned members in a given group. Only accessible to group Admins and above. Not '
            'applicable to all groups. Check group features.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_GroupV2-GetBannedMembersOfGroup.html'
            '#operation_get_GroupV2-GetBannedMembersOfGroup'
        ),
        method='GET'
    )
    def get_banned_members_of_group(
            self,
            group_id: int,
            page: Optional[int] = 1
    ) -> responses.GroupV2.GetBannedMembersOfGroup:
        return self.get(
            f'/{group_id}/Banned/',
            parameters=queries.GroupsV2.GetBannedMembersOfGroup(currentpage=page),
            response_format=responses.GroupV2.GetBannedMembersOfGroup
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Admin/AbdicateFoundership/{membershipType}/{founderIdNew}/',
        name='GroupV2.AbdicateFoundership',
        description=(
                'An administrative method to allow the founder of a group or clan to give up their position to another '
                'admin permanently.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-AbdicateFoundership.html'
            '#operation_post_GroupV2-AbdicateFoundership'
        ),
        method='POST'
    )
    def abdicate_foundership(
            self,
            group_id: int,
            membership_type: Union[int, BungieMembershipType],
            founder_id_new
    ) -> responses.GroupV2.AbdicateFoundership:
        if not isinstance(membership_type, BungieMembershipType):
            membership_type = BungieMembershipType(membership_type)

        return self.post(
            f'/{group_id}/Admin/AbdicateFoundership/{membership_type.value}/{founder_id_new}/',
            response_format=responses.GroupV2.AbdicateFoundership
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{group_id}/Members/Pending/',
        name='GroupV2.GetPendingMemberships',
        description=(
                'Gets the list of users who are awaiting a decision on their application to join a given group. '
                'Modified to include application info.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_GroupV2-GetPendingMemberships.html'
            '#operation_get_GroupV2-GetPendingMemberships'
        ),
        method='GET'
    )
    def get_pending_memberships(
            self,
            group_id: int,
            page: Optional[int] = 1
    ) -> responses.GroupV2.GetPendingMemberships:
        return self.get(
            f'/{group_id}/Members/Pending/',
            parameters=queries.GroupsV2.GetPendingMemberships(currentpage=page),
            response_format=responses.GroupV2.GetPendingMemberships
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Members/InvitedIndividuals/',
        name='GroupV2.GetInvitedIndividuals',
        description='Get the list of users who have been invited into the group.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_GroupV2-GetInvitedIndividuals.html'
            '#operation_get_GroupV2-GetInvitedIndividuals'
        ),
        method='GET'
    )
    def get_invited_individuals(
            self,
            group_id: int,
            page: Optional[int] = 1
    ) -> responses.GroupV2.GetInvitedIndividuals:
        return self.get(
            f'/{group_id}/Members/InvitedIndividuals/',
            parameters=queries.GroupsV2.GetInvitedIndividuals(currentpage=page),
            response_format=responses.GroupV2.GetInvitedIndividuals
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Members/ApproveAll/',
        name='GroupV2.ApproveAllPending',
        description='Approve all of the pending users for the given group.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-ApproveAllPending.html'
            '#operation_post_GroupV2-ApproveAllPending'
        ),
        method='POST'
    )
    def approve_all_pending(
            self,
            group_id: int,
            message: Optional[str] = None
    ) -> responses.GroupV2.ApproveAllPending:
        return self.post(
            f'/{group_id}/Members/ApproveAll/',
            body=queries.GroupsV2.GroupApplicationRequest(message=message),
            response_format=responses.GroupV2.ApproveAllPending
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Members/DenyAll/',
        name='GroupV2.DenyAllPending',
        description='Deny all of the pending users for the given group.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-DenyAllPending.html'
            '#operation_post_GroupV2-DenyAllPending'
        ),
        method='POST'
    )
    def deny_all_pending(
            self,
            group_id: int,
            message: Optional[str] = None
    ) -> responses.GroupV2.DenyAllPending:
        return self.post(
            f'/{group_id}/Members/DenyAll/',
            body=queries.GroupsV2.GroupApplicationRequest(message=message),
            response_format=responses.GroupV2.DenyAllPending
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Members/ApproveList/',
        name='GroupV2.ApprovePendingForList',
        description='Approve all of the pending users for the given group that match the given users.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-ApprovePendingForList.html'
            '#operation_post_GroupV2-ApprovePendingForList'
        ),
        method='POST'
    )
    def approve_pending_for_list(
            self,
            group_id: int,
            memberships: Union[List[Dict[str, Union[int, str]]], List[UserMembership]],
            message: Optional[str]
    ) -> responses.GroupV2.ApprovePendingForList:
        return self.post(
            f'/{group_id}/Members/ApproveList/',
            body=queries.GroupsV2.GroupApplicationListRequest(
                memberships=memberships,
                message=message
            ),
            response_format=responses.GroupV2.ApprovePendingForList
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Members/Approve/{membershipType}/{membershipId}/',
        name='GroupV2.ApprovePending',
        description='Approve the given membership id to join the group/clan as long as they have applied.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-ApprovePending.html'
            '#operation_post_GroupV2-ApprovePending'
        ),
        method='POST'
    )
    def approve_pending(
            self,
            group_id: int,
            membership_id: int,
            membership_type: Union[int, BungieMembershipType],
            message: Optional[str] = None
    ) -> responses.GroupV2.ApprovePending:
        if not isinstance(membership_type, BungieMembershipType):
            membership_type = BungieMembershipType(membership_type)

        return self.post(
            f'/{group_id}/Members/Approve/{membership_type.value}/{membership_id}/',
            body=queries.GroupsV2.GroupApplicationRequest(message=message),
            response_format=responses.GroupV2.ApprovePending
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Members/DenyList/',
        name='GroupV2.DenyPendingForList',
        description='Deny all of the pending users for the given group that match the given users.',
        href=(
                'https://bungie-net.github.io/multi/operation_post_GroupV2-DenyPendingForList.html'
                '#operation_post_GroupV2-DenyPendingForList'
        ),
        method='POST'
    )
    def deny_pending_for_list(
            self,
            group_id: int,
            memberships: Union[List[Dict[str, Union[int, str]]], List[UserMembership]],
            message: Optional[str]
    ) -> responses.GroupV2.DenyPendingForList:
        return self.post(
            f'/{group_id}/Members/DenyList/',
            body=queries.GroupsV2.GroupApplicationListRequest(
                memberships=memberships,
                message=message
            ),
            response_format=responses.GroupV2.DenyPendingForList
        )

    @endpoint(
        path='/GroupV2/User/{membershipType}/{membershipId}/{filter}/{groupType}/',
        name='GroupV2.GetGroupsForMember',
        description='Get information about the groups that a given member has joined.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_GroupV2-GetGroupsForMember.html'
            '#operation_get_GroupV2-GetGroupsForMember'
        ),
        method='GET'
    )
    def get_groups_for_member(
            self,
            membership_id: int,
            membership_type: Union[int, BungieMembershipType],
            group_type: Union[int, GroupType] = GroupType.Clan,
            group_filter: Union[int, GroupsForMemberFilter] = GroupsForMemberFilter.All
    ) -> responses.GroupV2.GetGroupsForMember:
        if not isinstance(membership_type, BungieMembershipType):
            membership_type = BungieMembershipType(membership_type)
        if not isinstance(group_type, GroupType):
            group_type = GroupType(group_type)
        if not isinstance(group_filter, GroupsForMemberFilter):
            group_filter = GroupsForMemberFilter(group_filter)

        return self.get(
            f'/User/{membership_type.value}/{membership_id}/{group_filter.value}/{group_type.value}/',
            response_format=responses.GroupV2.GetGroupsForMember
        )

    @endpoint(
        path='/GroupV2/Recover/{membershipType}/{membershipId}/{groupType}/',
        name='GroupV2.RecoverGroupForFounder',
        description='Allows a founder to manually recover a group they can see in game but not on Bungie.net',
        href=(
            'https://bungie-net.github.io/multi/operation_get_GroupV2-RecoverGroupForFounder.html'
            '#operation_get_GroupV2-RecoverGroupForFounder'
        ),
        method='GET'
    )
    def recover_group_for_founder(
            self,
            membership_id: int,
            membership_type: Union[int, BungieMembershipType],
            group_type: Union[int, GroupType] = GroupType.Clan
    ) -> responses.GroupV2.RecoverGroupForFounder:
        if not isinstance(membership_type, BungieMembershipType):
            membership_type = BungieMembershipType(membership_type)
        if not isinstance(group_type, GroupType):
            group_type = GroupType(group_type)

        return self.get(
            f'/Recover/{membership_type.value}/{membership_id}/{group_type.value}/',
            response_format=responses.GroupV2.RecoverGroupForFounder
        )

    @endpoint(
        path='/GroupV2/User/Potential/{membershipType}/{membershipId}/{filter}/{groupType}/',
        name='GroupV2.GetPotentialGroupsForMember',
        description='Get information about the groups that a given member has applied to or been invited to.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_GroupV2-GetPotentialGroupsForMember.html'
            '#operation_get_GroupV2-GetPotentialGroupsForMember'
        ),
        method='GET'
    )
    def get_potential_groups_for_member(
            self,
            membership_id: int,
            membership_type: Union[int, BungieMembershipType],
            group_type: Union[int, GroupType] = GroupType.Clan,
            group_filter: Union[int, GroupsForMemberFilter] = GroupsForMemberFilter.All
    ) -> responses.GroupV2.GetPotentialGroupsForMember:
        if not isinstance(membership_type, BungieMembershipType):
            membership_type = BungieMembershipType(membership_type)
        if not isinstance(group_type, GroupType):
            group_type = GroupType(group_type)
        if not isinstance(group_filter, GroupsForMemberFilter):
            group_filter = GroupsForMemberFilter(group_filter)

        return self.get(
            f'/User/Potential/{membership_type.value}/{membership_id}/{group_filter.value}/{group_type.value}/',
            response_format=responses.GroupV2.GetPotentialGroupsForMember
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Members/IndividualInvite/{membershipType}/{membershipId}/',
        name='GroupV2.IndividualGroupInvite',
        description='Invite a specified user to join a group.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-IndividualGroupInvite.html'
            '#operation_post_GroupV2-IndividualGroupInvite'
        ),
        method='POST'
    )
    def individual_group_invite(
            self,
            group_id: int,
            membership_id: int,
            membership_type: Union[int, BungieMembershipType],
            message: Optional[str] = None
    ) -> responses.GroupV2.IndividualGroupInvite:
        if not isinstance(membership_type, BungieMembershipType):
            membership_type = BungieMembershipType(membership_type)

        return self.post(
            f'/{group_id}/Members/IndividualInvite/{membership_type.value}/{membership_id}/',
            body=queries.GroupsV2.GroupApplicationRequest(message=message),
            response_format=responses.GroupV2.IndividualGroupInvite
        )

    @oauth_required(ApplicationScopes.AdminGroups)
    @endpoint(
        path='/GroupV2/{groupId}/Members/IndividualInviteCancel/{membershipType}/{membershipId}/',
        name='GroupV2.IndividualGroupInviteCancel',
        description='Cancels a pending invite to join a group.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_GroupV2-IndividualGroupInviteCancel.html'
            '#operation_post_GroupV2-IndividualGroupInviteCancel'
        ),
        method='POST'
    )
    def individual_group_invite_cancel(
            self,
            group_id: int,
            membership_id: int,
            membership_type: Union[int, BungieMembershipType]
    ) -> responses.GroupV2.IndividualGroupInviteCancel:
        if not isinstance(membership_type, BungieMembershipType):
            membership_type = BungieMembershipType(membership_type)

        return self.post(
            f'/{group_id}/Members/IndividualInviteCancel/{membership_type.value}/{membership_id}/',
            response_format=responses.GroupV2.IndividualGroupInviteCancel
        )


def setup(client: Union[SyncClient, AsyncClient, SubClient]) -> None:
    client.add_subclient(GroupV2())
