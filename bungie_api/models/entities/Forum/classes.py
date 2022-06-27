from typing import List, Optional

from arya_api_framework import BaseModel
from pydantic import Extra

from ....utils import ValidatedDatetime
from ..User import GeneralUser
from ..GroupsV2 import GroupResponse
from ..Tags.Models.Contracts import TagResponse
from ..Queries import PagedQuery
from ..Ignores import IgnoreResponse


__all__ = [
    'PostResponse',
    'PollResult',
    'PollResponse',
    'ForumRecruitmentDetail',
    'PostSearchResponse',
]


class PostResponse(BaseModel):
    postId: int
    parentPostId: Optional[int]
    topicId: Optional[int]
    forumId: Optional[int]
    threadDepth: int
    category: int
    authorMembershipId: int
    editorMembershipId: Optional[int]
    subject: Optional[str]
    body: Optional[str]
    tags: Optional[List[str]]
    urlLinkOrImage: str
    creationDate: ValidatedDatetime
    lastModified: ValidatedDatetime
    editCount: int
    replyCount: int
    topicReplyCount: int
    ratingCount: int
    rating: int
    upvotes: int
    downvotes: int
    ratingScore: int
    isGroupPrivate: bool
    flags: int
    lockedForReplies: bool
    parentAuthorId: int
    topicAuthorId: int
    isTopicBanned: bool
    actualParentPostId: Optional[int]
    playerSupportFlags: int
    pinned: int
    awaitingApproval: bool
    lastReplyTimestamp: ValidatedDatetime
    lastReplyDate: Optional[ValidatedDatetime]
    archivedLastReplyDate: Optional[ValidatedDatetime]
    lastReplyId: Optional[int]
    IsPinned: bool
    urlMediaType: int
    thumbnail: Optional[str]
    popularity: int
    isActive: bool
    isAnnouncement: bool
    userRating: int
    userHasRated: bool
    userHasMutedPost: bool
    latestReplyPostId: int
    latestReplyAuthorId: int
    ignoreStatus: IgnoreResponse
    locale: str
    metadata: Optional[int]


class PollResult(BaseModel):
    answerText: str
    answerSlot: int
    lastVoteDate: ValidatedDatetime
    votes: int
    requestingUserVoted: bool


class PollResponse(BaseModel):
    topicId: int
    results: List[PollResult]
    totalVotes: int


class ForumRecruitmentDetail(BaseModel):
    topicId: int
    microphoneRequired: bool
    intensity: str
    tone: str
    approved: bool
    conversationId: Optional[int]
    playerSlotsTotal: int
    playerSlotsRemaining: int
    Fireteam: List[GeneralUser]
    kickedPlayerIds: List[int]


class PostSearchResponse(BaseModel):
    relatedPosts: List[PostResponse]
    authors: List[GeneralUser]
    groups: List[GroupResponse]
    searchedTags: List[TagResponse]
    polls: List[PollResponse]
    recruitmentDetails: List[ForumRecruitmentDetail]
    availablePages: Optional[int]
    results: List[PostResponse]
    totalResults: int
    hasMore: bool
    query: PagedQuery
    replacementContinuationToken: Optional[str]
    useTotalResults: bool
