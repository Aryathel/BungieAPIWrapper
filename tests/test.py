import logging
import os

from arya_api_framework import BaseModel
from dotenv import load_dotenv
from pydantic import Extra

from bungie_api import BungieAPI

load_dotenv()

logging.basicConfig(level=logging.INFO)

API_KEY = os.getenv('BUNGIE_API_KEY')
CLIENT_ID = os.getenv('BUNGIE_CLIENT_ID')
CLIENT_ID = int(CLIENT_ID) if CLIENT_ID else CLIENT_ID


class TestResponses(BaseModel):
    class Config:
        extra = Extra.allow


def auth_user() -> None:
    # User OAuth
    api.oauth.user_auth_local()


def test_app_endpoints(api: BungieAPI, dt: TestResponses) -> None:
    # App Endpoints
    content = {}

    # - You almost always lack permissions for this, so it is excluded in testing.
    # r = api.app.get_application_api_usage()
    content[api.app.get_application_api_usage.__endpoint_name__] = "DISABLED"

    # - This won't change much, these are Bungie-owned applications (e.g. their website, D2 companion app, etc.)
    r = api.app.get_bungie_applications()
    content[api.app.get_bungie_applications.__endpoint_name__] = r.dict()

    setattr(dt, api.app.name, content)


def test_user_endpoints(api: BungieAPI, dt: TestResponses) -> None:
    content = {}
    # User Endpoints
    user = api.user.get_current_bungie_net_user()
    content[api.user.get_current_bungie_net_user.__endpoint_name__] = user.dict()

    r = api.user.get_bungie_net_user_by_id(user.Response.membershipId)
    content[api.user.get_bungie_net_user_by_id.__endpoint_name__] = r.dict()

    r = api.user.get_sanitized_platform_display_names(user.Response.membershipId)
    content[api.user.get_sanitized_platform_display_names.__endpoint_name__] = r.dict()

    r = api.user.get_credential_types_for_target_account(user.Response.membershipId)
    content[api.user.get_credential_types_for_target_account.__endpoint_name__] = r.dict()

    r = api.user.get_memberships_by_id(user.Response.membershipId, 3)
    content[api.user.get_memberships_by_id.__endpoint_name__] = r.dict()

    r = api.user.get_available_themes()
    content[api.user.get_available_themes.__endpoint_name__] = r.dict()

    r = api.user.get_memberships_for_current_user()
    content[api.user.get_memberships_for_current_user.__endpoint_name__] = r.dict()

    r = api.user.get_membership_from_hard_linked_credential(76561198119241330)
    content[api.user.get_membership_from_hard_linked_credential.__endpoint_name__] = r.dict()

    r = api.user.search_by_global_name_post("Arya")
    content[api.user.search_by_global_name_post.__endpoint_name__] = r.dict()

    setattr(dt, api.user.name, content)


def test_content_endpoints(api: BungieAPI, dt: TestResponses) -> None:
    # Content Endpoints
    # The only content types I know of right now are "Help", "News", and "ContentSet",
    # other types will have the ``Response`` field set to ``None``.
    content = {}

    r = api.content.get_content_type('News')
    content[api.content.get_content_type.__endpoint_name__] = r.dict()

    r = api.content.get_content_by_id(51481)
    content[api.content.get_content_by_id.__endpoint_name__] = r.dict()

    r = api.content.get_content_by_tag_and_type('destiny 2', 'News')
    content[api.content.get_content_by_tag_and_type.__endpoint_name__] = r.dict()

    r = api.content.search_content_with_text('News', 'Crucible')
    content[api.content.search_content_with_text.__endpoint_name__] = r.dict()

    r = api.content.search_content_by_tag_and_type('destiny 2', 'News')
    content[api.content.search_content_by_tag_and_type.__endpoint_name__] = r.dict()

    setattr(dt, api.content.name, content)


def test_forum_endpoints(api: BungieAPI, dt: TestResponses) -> None:
    # Forum endpoints
    content = {}

    r = api.forum.get_topics_paged()
    content[api.forum.get_topics_paged.__endpoint_name__] = r.dict()

    r = api.forum.get_core_topics_paged()
    content[api.forum.get_core_topics_paged.__endpoint_name__] = r.dict()

    r = api.forum.get_posts_threaded_paged(1)
    content[api.forum.get_posts_threaded_paged.__endpoint_name__] = r.dict()

    r = api.forum.get_posts_threaded_paged_from_child(237834058)
    content[api.forum.get_posts_threaded_paged_from_child.__endpoint_name__] = r.dict()

    r = api.forum.get_post_and_parent(261314609)
    content[api.forum.get_post_and_parent.__endpoint_name__] = r.dict()

    # You almost always lack permissions for this, so it excluded in testing.
    # r = api.forum.get_post_and_parent_awaiting_approval(261314609)
    content[api.forum.get_post_and_parent_awaiting_approval.__endpoint_name__] = "DISABLED"

    # I couldn't find a content piece that this applied to, and it throws an error if the topic doesn't exist
    # for the given content, so I am removing it from testing.
    # r = api.forum.get_topic_for_content(51454)
    content[api.forum.get_topic_for_content.__endpoint_name__] = "DISABLED"

    # Seems to always result in an error saying that the partial tag is invalid.
    # Therefore, this is being excluded from testing.
    # r = api.forum.get_forum_tag_suggestions('start')
    content[api.forum.get_forum_tag_suggestions.__endpoint_name__] = "DISABLED"

    r = api.forum.get_poll(261313583)
    content[api.forum.get_poll.__endpoint_name__] = r.dict()

    # Disabled at the time of writing, so removing from testing.
    # r = api.forum.get_recruitment_thread_summaries([261312591])
    content[api.forum.get_recruitment_thread_summaries.__endpoint_name__] = "DISABLED"

    setattr(dt, api.forum.name, content)


def test_groupv2_endpoints(api: BungieAPI, dt: TestResponses) -> None:
    # GroupV2 Endpoints
    content = {}

    r = api.groupv2.get_available_avatars()
    content[api.groupv2.get_available_avatars.__endpoint_name__] = r.dict()

    r = api.groupv2.get_available_themes()
    content[api.groupv2.get_available_themes.__endpoint_name__] = r.dict()

    r = api.groupv2.get_user_clan_invite_setting(3)
    content[api.groupv2.get_user_clan_invite_setting.__endpoint_name__] = r.dict()

    # Standard applications will not have access to this endpoint,
    # it requires the ``ReadUserData`` oauth scope, which cannot be assigned for a normal
    # application. Therefore, this is excluded from testing.
    # r = api.groupv2.get_recommended_groups(0, '0')
    content[api.groupv2.get_recommended_groups.__endpoint_name__] = "DISABLED"

    r = api.groupv2.group_search('UArizona Gaming', 1, creation_date=1)
    content[api.groupv2.group_search.__endpoint_name__] = r.dict()

    r = api.groupv2.get_group(2603136)
    content[api.groupv2.get_group.__endpoint_name__] = r.dict()

    r = api.groupv2.get_group_by_name('UArizona Gaming', 1)
    content[api.groupv2.get_group_by_name.__endpoint_name__] = r.dict()

    r = api.groupv2.get_group_by_name_v2('UArizona Gaming', 1)
    content[api.groupv2.get_group_by_name_v2.__endpoint_name__] = r.dict()

    r = api.groupv2.get_group_optional_conversations(2603136)
    content[api.groupv2.get_group_optional_conversations.__endpoint_name__] = r.dict()

    # Disabled from testing since there is a limit on the rate at which clans can be edited,
    # and I don't want to edit my own clan every time I test this. It works.
    # r = api.groupv2.edit_group(group_id=2603136, motto='Eyes up, Wildcats.')
    content[api.groupv2.edit_group.__endpoint_name__] = "DISABLED"

    # Disabled because I do not want to keep setting the clan banner to the same thing.
    # It works as intended.
    # r = api.groupv2.edit_clan_banner(
    #     2603136,
    #     decal_id=4142223386,
    #     decal_color_id=3379387803,
    #     decal_background_color_id=3568748754,
    #     gonfalon_id=1473910866,
    #     gonfalon_color_id=2140858746,
    #     gonfalon_detail_id=1681253715,
    #     gonfalon_detail_color_id=4128900497
    # )
    content[api.groupv2.edit_clan_banner.__endpoint_name__] = "DISABLED"

    r = api.groupv2.edit_founder_options(
        2603136,
        join_level=2,
        invite_permission_override=True
    )
    content[api.groupv2.edit_founder_options.__endpoint_name__] = r.dict()

    # Disabled for testing because I do not want to create a new channel every time I test.
    # It works as intended.
    # r = api.groupv2.add_optional_conversation(
    #     2603136,
    #     chat_name='Testing',
    #     chat_security=1
    # )
    content[api.groupv2.add_optional_conversation.__endpoint_name__] = "DISABLED"

    # Disabled for testing because I do not want to always mess with clan settings.
    # It works as intended.
    # r = api.groupv2.edit_optional_conversation(
    #     2603136,
    #     71040474,
    #     chat_enabled=False,
    #     chat_name='Testing Again'
    # )
    content[api.groupv2.edit_optional_conversation.__endpoint_name__] = "DISABLED"

    r = api.groupv2.get_members_of_group(2603136, name_search='A')
    content[api.groupv2.get_members_of_group.__endpoint_name__] = r.dict()

    r = api.groupv2.get_admins_and_founder_of_group(2603136)
    content[api.groupv2.get_admins_and_founder_of_group.__endpoint_name__] = r.dict()

    # Disabled for testing because I don't want to have to update a clan member every time.
    # It works as intended.
    # r = api.groupv2.edit_group_membership(
    #     2603136,
    #     membership_id=4611686018470787010,
    #     membership_type=3,
    #     member_type=3
    # )
    content[api.groupv2.edit_group_membership.__endpoint_name__] = "DISABLED"

    # Disabled for testing because kicking people gets old.
    # It works as intended.
    # r = api.groupv2.kick_member(
    #     2603136,
    #     4611686018468651276,
    #     membership_type=3
    # )
    content[api.groupv2.kick_member.__endpoint_name__] = "DISABLED"

    # Disabled for testing, because I don't want to eep banning people.
    # It works as intended.
    # r = api.groupv2.ban_member(
    #     2603136,
    #     4611686018471155055,
    #     3,
    #     "I needed a guinea pig for testing."
    # )
    content[api.groupv2.ban_member.__endpoint_name__] = "DISABLED"

    # Disabled for testing, there are no more banned members to test against.
    # It works as intended.
    # r = api.groupv2.unban_member(
    #     2603136,
    #     4611686018471155055,
    #     3
    # )
    content[api.groupv2.unban_member.__endpoint_name__] = "DISABLED"

    r = api.groupv2.get_banned_members_of_group(2603136)
    content[api.groupv2.get_banned_members_of_group.__endpoint_name__] = r.dict()

    # Disabled because this requires a priveleged OAuth scope that
    # most clients cannot use.
    # r = api.groupv2.abdicate_foundership(2603136, 3, 0000)
    content[api.groupv2.abdicate_foundership.__endpoint_name__] = "DISABLED"

    r = api.groupv2.get_pending_memberships(2603136)
    content[api.groupv2.get_pending_memberships.__endpoint_name__] = r.dict()

    r = api.groupv2.get_invited_individuals(2603136)
    content[api.groupv2.get_invited_individuals.__endpoint_name__] = r.dict()

    # r = api.groupv2.approve_all_pending(2603136, "Approving new members.")
    content[api.groupv2.approve_all_pending.__endpoint_name__] = "DISABLED"

    # r = api.groupv2.deny_all_pending(2603136, "Denying new members.")
    content[api.groupv2.deny_all_pending.__endpoint_name__] = "DISABLED"

    r = api.groupv2.approve_pending_for_list(
        2603136,
        memberships=[{"membershipType": 3, "membershipId": 4611686018483530949}],
        message='Group approving.'
    )
    content[api.groupv2.approve_pending_for_list.__endpoint_name__] = r.dict()

    # r = api.groupv2.approve_pending(2603136, 4611686018483530949, 3, 'Testing.')
    content[api.groupv2.approve_pending.__endpoint_name__] = "DISABLED"

    r = api.groupv2.deny_pending_for_list(
        2603136,
        memberships=[{"membershipType": 3, "membershipId": 4611686018483530949}],
        message='Group approving.'
    )
    content[api.groupv2.deny_pending_for_list.__endpoint_name__] = r.dict()

    r = api.groupv2.get_groups_for_member(
        4611686018483530949,
        3,
        1
    )
    content[api.groupv2.get_groups_for_member.__endpoint_name__] = r.dict()

    # Most applications do not have permission to use this.
    # r = api.groupv2.recover_group_for_founder(4611686018483530949, 3, 1)
    content[api.groupv2.recover_group_for_founder.__endpoint_name__] = "DISABLED"

    r = api.groupv2.get_potential_groups_for_member(4611686018483530949, 3)
    content[api.groupv2.get_potential_groups_for_member.__endpoint_name__] = r.dict()

    # r = api.groupv2.individual_group_invite(
    #     2603136,
    #     4611686018483530949,
    #     3
    # )
    content[api.groupv2.individual_group_invite.__endpoint_name__] = "DISABLED"

    r = api.groupv2.individual_group_invite_cancel(
        2603136,
        4611686018483530949,
        3
    )
    content[api.groupv2.individual_group_invite_cancel.__endpoint_name__] = r.dict()

    setattr(dt, api.groupv2.name, content)


def test_token_endpoints(api: BungieAPI, dt: TestResponses) -> None:
    # Tokens Endpoints
    content = {}

    # Most clients cannot get ``PartnerOfferGrant`` scopes,
    # so this is disabled.
    # r = api.tokens.claim_partner_offer(partner_offer_id="0", bungie_net_membership_id=0, transaction_id="0")
    content[api.tokens.claim_partner_offer.__endpoint_name__] = "DISABLED"

    # Most clients cannot get ``PartnerOfferGrant`` scopes,
    # so this is disabled.
    # r = api.tokens.apply_missing_partner_offers_without_claim(
    #     19548659,
    #     0000
    # )
    content[api.tokens.apply_missing_partner_offers_without_claim.__endpoint_name__] = "DISABLED"

    # Most clients cannot get ``PartnerOfferGrant`` scopes,
    # so this is disabled.
    # r = api.tokens.get_partner_offer_sku_history(19548659, 0000)
    content[api.tokens.get_partner_offer_sku_history.__endpoint_name__] = "DISABLED"

    # Most clients cannot get ``ReadAndApplyToken`` scopes,
    # so this is disabled.
    # r = api.tokens.get_bungie_rewards_for_user(19548659)
    content[api.tokens.get_bungie_rewards_for_user.__endpoint_name__] = "DISABLED"

    r = api.tokens.get_bungie_rewards_list()
    content[api.tokens.get_bungie_rewards_list.__endpoint_name__] = r.dict()

    setattr(dt, api.tokens.name, content)


def test_destiny2_endpoints(api: BungieAPI, dt: TestResponses) -> None:
    # Destiny2 Endpoints
    content = {}

    r = api.destiny2.get_destiny_manifest()
    content[api.destiny2.get_destiny_manifest.__endpoint_name__] = r.dict()

    r = api.destiny2.get_destiny_entity_definition(
        'DestinyClassDefinition',
        671679327
    )
    content[api.destiny2.get_destiny_entity_definition.__endpoint_name__] = r.dict()

    user = api.destiny2.search_destiny_player_by_bungie_name(
        'Aryathel',
        7877,
        3
    )
    content[api.destiny2.search_destiny_player_by_bungie_name.__endpoint_name__] = user.dict()

    r = api.destiny2.get_linked_profiles(
        user.Response[0].membershipId,
        user.Response[0].membershipType
    )
    content[api.destiny2.get_linked_profiles.__endpoint_name__] = r.dict()

    r = api.destiny2.get_profile(
        user.Response[0].membershipId,
        user.Response[0].membershipType,
        [
            100, 101, 102, 103, 104, 105, 200, 201, 202, 203, 204, 205, 300, 301, 302, 303, 304, 305, 306, 307, 308,
            309, 310, 400, 401, 402, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300
        ]
    )
    content[api.destiny2.get_profile.__endpoint_name__] = r.dict()

    print(r)

    setattr(dt, api.destiny2.name, content)


if __name__ == "__main__":
    api = BungieAPI(API_KEY, CLIENT_ID)
    # print(api.tree(serialized=True, indent=2))

    dt = TestResponses()
    auth_user()
    # test_app_endpoints(api, dt)
    # test_user_endpoints(api, dt)
    # test_content_endpoints(api, dt)
    # test_forum_endpoints(api, dt)
    # test_groupv2_endpoints(api, dt)
    # test_token_endpoints(api, dt)
    test_destiny2_endpoints(api, dt)

    with open('results.json', 'w+') as f:
        f.write(dt.json(indent=2))

    api.close()
