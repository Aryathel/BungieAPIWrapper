from typing import Union, Optional, List

from arya_api_framework import SyncClient, AsyncClient, SubClient
from arya_api_framework.utils import apiclient, endpoint

from ..models import responses, queries
from ..models.entities.Forum import (
    ForumTopicsCategoryFiltersEnum,
    ForumTopicsQuickDateEnum,
    ForumTopicsSortEnum,
    ForumThreadSortEnum,
)


__all__ = [
    'Forum',
]


@apiclient
class Forum(SubClient, name='forum', relative_path='/Forum'):
    @endpoint(
        path='/Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/',
        name='Forum.GetTopicsPaged',
        description='Get topics from any forum.',
        href=(
                'https://bungie-net.github.io/multi/operation_get_Forum-GetTopicsPaged.html'
                '#operation_get_Forum-GetTopicsPaged'
        ),
        method='GET'
    )
    def get_topics_paged(
            self,
            page: Optional[int] = 0,
            page_size: Optional[int] = 0,
            group: Optional[int] = 0,
            sort: Optional[Union[int, ForumTopicsSortEnum]] = ForumTopicsSortEnum.Default,
            quick_date: Optional[Union[int, ForumTopicsQuickDateEnum]] = ForumTopicsQuickDateEnum.All,
            category_filter: Optional[
                Union[int, ForumTopicsCategoryFiltersEnum]
            ] = ForumTopicsCategoryFiltersEnum.None_,
            locales: Optional[Union[str, List[str]]] = 'en',
            tagstring: Optional[str] = None,
    ) -> responses.Forum.GetTopicsPaged:
        if not isinstance(sort, ForumTopicsSortEnum):
            sort = ForumTopicsSortEnum(sort)
        if not isinstance(quick_date, ForumTopicsQuickDateEnum):
            quick_date = ForumTopicsQuickDateEnum(quick_date)
        if not isinstance(category_filter, ForumTopicsCategoryFiltersEnum):
            category_filter = ForumTopicsCategoryFiltersEnum(category_filter)
        if isinstance(locales, list):
            locales = ', '.join(locales)

        return self.get(
            f'/GetTopicsPaged/{page}/{page_size}/{group}/{sort.value}/{quick_date.value}/{category_filter.value}/',
            parameters=queries.Forum.GetTopicsPaged(
                locales=locales,
                tagstring=tagstring,
            ),
            response_format=responses.Forum.GetTopicsPaged
        )

    @endpoint(
        path='/Forum/GetCoreTopicsPaged/{page}/{sort}/{quickDate}/{categoryFilter}/',
        name='Forum.GetCoreTopicsPages',
        description='Gets a listing of all topics marked as part of the core group.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Forum-GetCoreTopicsPaged.html'
            '#operation_get_Forum-GetCoreTopicsPaged'
        ),
        method='GET'
    )
    def get_core_topics_paged(
            self,
            page: int = 0,
            sort: Optional[Union[int, ForumTopicsSortEnum]] = ForumTopicsSortEnum.Default,
            quick_date: Optional[Union[int, ForumTopicsQuickDateEnum]] = ForumTopicsQuickDateEnum.All,
            category_filter: Optional[
                Union[int, ForumTopicsCategoryFiltersEnum]
            ] = ForumTopicsCategoryFiltersEnum.None_,
            locales: Optional[Union[str, List[str]]] = 'en'
    ) -> responses.Forum.GetCoreTopicsPaged:
        if not isinstance(sort, ForumTopicsSortEnum):
            sort = ForumTopicsSortEnum(sort)
        if not isinstance(quick_date, ForumTopicsQuickDateEnum):
            quick_date = ForumTopicsQuickDateEnum(quick_date)
        if not isinstance(category_filter, ForumTopicsCategoryFiltersEnum):
            category_filter = ForumTopicsCategoryFiltersEnum(category_filter)
        if isinstance(locales, list):
            locales = ', '.join(locales)

        return self.get(
            f'/GetCoreTopicsPaged/{page}/{sort.value}/{quick_date.value}/{category_filter.value}/',
            parameters=queries.Forum.GetCoreTopicsPaged(locales=locales),
            response_format=responses.Forum.GetCoreTopicsPaged
        )

    @endpoint(
        path='/Forum/GetPostsThreadedPaged/{parentPostId}/{page}/{pageSize}/{replySize}/{getParentPost}/{rootThreadMode}/{sortMode}/',
        name='Forum.GetPostsThreadedPaged',
        description=(
            'Returns a thread of posts at the given parent, optionally returning replies to those posts as well as the '
            'original parent.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Forum-GetPostsThreadedPaged.html'
            '#operation_get_Forum-GetPostsThreadedPaged'
        ),
        method='GET'
    )
    def get_posts_threaded_paged(
            self,
            parent_post_id: int,
            page: Optional[int] = 0,
            page_size: Optional[int] = 5,  # Defaults to minimum number of pages to work.
            reply_size: Optional[int] = 0,
            get_parent_post: Optional[bool] = False,
            root_thread_mode: Optional[bool] = False,
            sort: Optional[Union[int, ForumThreadSortEnum]] = ForumThreadSortEnum.Newest,
            show_banned: Optional[bool] = False
    ) -> responses.Forum.GetPostsThreadedPaged:
        """

        Arguments:
            parent_post_id: :py:class:`int`
                The ID of the parent post from which to retrieve the thread of posts.
            page: Optional[:py:class:`int`]
                The page of responses to return, starting with ``0``. Defaults to ``0``.
            page_size: Optional[:py:class:`int`]
                The number of items per page to return in the response. The actual number of posts returned seems to be
                1 more than this argument, but the next page will include that final extra post as its first element.
                (e.g. :paramref:`page_size` ``5``, :paramref:`page` ``0`` will return posts ``1, 2, 3, 4, 5, 6``,
                :paramref:`page` ``1`` will return posts ``6, 7, 8, 9, 10, 11``) Defaults to the minimum page size,
                ``5``.
            reply_size: Optional[:py:class:`int`]
                Seems to currently have no effect. Defaults to ``0``.
            get_parent_post: Optional[:py:class:`bool`]
                Whether or not to include the parent post in the responses. If this is ``True``, every response
                will include the post with id matching :paramref:`parent_post_id` as the first response in the list of
                responses. Defaults to ``False``.

                Note
                ----
                    This also adds 1 to the number of responses defined by :paramref:`page_size`. So a page size of
                    ``5`` will return up to 6 items by default, and up to 7 with :paramref:`get_parent_post` set to
                    ``True``.
            root_thread_mode: Optional[:py:class:`bool`]
                Seems to currently have no effect. Defaults to ``False``.
            sort: Optional[Union[:py:class:`int`, :class:`ForumThreadSortEnum`]]
                The sorting method for the returned responses. ``0`` will return the newest posts first,
                ``1`` will return the oldest posts first. Defaults to :attr:`ForumThreadSortEnum.Newest`.
            show_banned: Optional[:py:class:`bool`]
                Whether to include banned posts in the responses. Defaults to ``False``.
        """
        if not isinstance(sort, ForumThreadSortEnum):
            sort = ForumThreadSortEnum(sort)

        return self.get(
            f'/GetPostsThreadedPaged/{parent_post_id}/{page}/{page_size}/{reply_size}/{get_parent_post}'
            f'/{root_thread_mode}/{sort.value}',
            parameters=queries.Forum.GetPostsThreadedPaged(showbanned=show_banned if show_banned else None),
            response_format=responses.Forum.GetPostsThreadedPaged
        )

    @endpoint(
        path='/Forum/GetPostsThreadedPagedFromChild/{childPostId}/{page}/{pageSize}/{replySize}/{rootThreadMode}/{sortMode}/',
        name='Forum.GetPostsThreadedPagedFromChild',
        description=(
                'Returns a thread of posts starting at the topicId of the input childPostId, optionally returning '
                'replies to those posts as well as the original parent.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Forum-GetPostsThreadedPagedFromChild.html'
            '#operation_get_Forum-GetPostsThreadedPagedFromChild'
        ),
        method='GET'
    )
    def get_posts_threaded_paged_from_child(
            self,
            child_post_id: int,
            page: Optional[int] = 0,
            page_size: Optional[int] = 5,
            reply_size: Optional[int] = 0,
            root_thread_mode: Optional[bool] = False,
            sort: Optional[Union[int, ForumThreadSortEnum]] = ForumThreadSortEnum.Newest,
            show_banned: Optional[bool] = False
    ) -> responses.Forum.GetPostsThreadedPagedFromChild:
        if not isinstance(sort, ForumThreadSortEnum):
            sort = ForumThreadSortEnum(sort)

        return self.get(
            f'/GetPostsThreadedPagedFromChild/{child_post_id}/{page}/{page_size}/{reply_size}/{root_thread_mode}'
            f'/{sort.value}/',
            parameters=queries.Forum.GetPostsThreadedPagedFromChild(showbanned=show_banned if show_banned else None),
            response_format=responses.Forum.GetPostsThreadedPagedFromChild
        )

    @endpoint(
        path='/Forum/GetPostAndParent/{childPostId}/',
        name='Forum.GetPostAndParent',
        description='Returns the post specified and its immediate parent.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Forum-GetPostAndParent.html'
            '#operation_get_Forum-GetPostAndParent'
        ),
        method='GET'
    )
    def get_post_and_parent(
            self,
            child_post_id: int,
            show_banned: Optional[bool] = False
    ) -> responses.Forum.GetPostAndParent:
        return self.get(
            f'/GetPostAndParent/{child_post_id}/',
            parameters=queries.Forum.GetPostAndParent(showbanned=show_banned),
            response_format=responses.Forum.GetPostAndParent
        )

    @endpoint(
        path='/Forum/GetPostAndParentAwaitingApproval/{childPostId}/',
        name='Forum.GetPostAndParentAwaitingApproval',
        description='Returns the post specified and its immediate parent of posts that are awaiting approval.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Forum-GetPostAndParentAwaitingApproval.html'
            '#operation_get_Forum-GetPostAndParentAwaitingApproval'
        ),
        method='GET'
    )
    def get_post_and_parent_awaiting_approval(
            self,
            child_post_id: int,
            show_banned: Optional[bool] = False
    ) -> responses.Forum.GetPostAndParentAwaitingApproval:
        return self.get(
            f'/GetPostAndParentAwaitingApproval/{child_post_id}/',
            parameters=queries.Forum.GetPostAndParentAwaitingApproval(showbanned=show_banned),
            response_format=responses.Forum.GetPostAndParentAwaitingApproval
        )

    @endpoint(
        path='/Forum/GetTopicForContent/{contentId}/',
        name='Forum.GetTopicForContent',
        description='Gets the post id for the given item\'s comments, if it exists.',
        href=(
            'https://bungie-net.github.io/multi/operation_get_Forum-GetTopicForContent.html'
            '#operation_get_Forum-GetTopicForContent'
        ),
        method='GET'
    )
    def get_topic_for_content(self, content_id: int) -> responses.Forum.GetTopicForContent:
        return self.get(
            f'/GetTopicForContent/{content_id}/',
            response_format=responses.Forum.GetTopicForContent
        )

    @endpoint(
        path='/Forum/GetForumTagSuggestions/',
        name='Forum.GetForumTagSuggestions',
        description=(
                'Gets tag suggestions based on partial text entry, matching them with other tags previously used in '
                'the forums.'
        ),
        href=(
            'https://bungie-net.github.io/multi/operation_get_Forum-GetForumTagSuggestions.html'
            '#operation_get_Forum-GetForumTagSuggestions'
        ),
        method='GET'
    )
    def get_forum_tag_suggestions(
            self,
            partial_tag: str
    ) -> responses.Forum.GetForumTagSuggestions:
        return self.get(
            '/GetForumTagSuggestions/',
            parameters=queries.Forum.GetForumTagSuggestions(partialtag=partial_tag),
            response_format=responses.Forum.GetForumTagSuggestions
        )

    @endpoint(
        path='/Forum/Poll/{topicId}/',
        name='Forum.GetPoll',
        description='Gets the specified forum poll.',
        href='https://bungie-net.github.io/multi/operation_get_Forum-GetPoll.html#operation_get_Forum-GetPoll',
        method='GET'
    )
    def get_poll(self, topic_id: int) -> responses.Forum.GetPoll:
        return self.get(f'/Poll/{topic_id}', response_format=responses.Forum.GetPoll)

    @endpoint(
        path='/Forum/Recruit/Summaries/',
        name='Forum.GetRecruitmentThreadSummaries',
        description='Allows the caller to get a list of up to 25 recruitment thread summary information objects.',
        href=(
            'https://bungie-net.github.io/multi/operation_post_Forum-GetRecruitmentThreadSummaries.html'
            '#operation_post_Forum-GetRecruitmentThreadSummaries'
        ),
        method='POST'
    )
    def get_recruitment_thread_summaries(
            self,
            thread_ids: Union[int, List[int]]
    ) -> responses.Forum.GetRecruitmentThreadSummaries:
        if not isinstance(thread_ids, list):
            thread_ids = [int(thread_ids)]
        else:
            thread_ids = [int(i) for i in thread_ids]

        return self.post(
            '/Recruit/Summaries/',
            body=thread_ids,
            response_format=responses.Forum.GetRecruitmentThreadSummaries
        )


def setup(client: Union[SyncClient, AsyncClient]) -> None:
    client.add_subclient(Forum())
