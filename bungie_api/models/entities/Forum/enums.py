from ..framework import DocumentedIntEnum, DocumentedIntFlag


__all__ = [
    'ForumTopicsCategoryFiltersEnum',
    'ForumTopicsQuickDateEnum',
    'ForumTopicsSortEnum',
    'ForumThreadSortEnum',
    'CommunityContentSortMode',
    'ForumMediaType',
    'ForumPostCategoryEnums',
    'ForumFlagsEnum',
    'ForumPostPopularity',
    'ForumRecruitmentIntensityLabel',
    'ForumRecruitmentToneLabel',
    'ForumPostSortEnum',
]


class ForumTopicsCategoryFiltersEnum(DocumentedIntFlag):
    None_ = 0
    Links = 1
    Questions = 2
    AnsweredQuestions = 4
    Media = 8
    TextOnly = 16
    Announcement = 32
    BungieOfficial = 64
    Polls = 128


class ForumTopicsQuickDateEnum(DocumentedIntEnum):
    All = 0
    LastYear = 1
    LastMonth = 2
    LastWeek = 3
    LastDay = 4


class ForumTopicsSortEnum(DocumentedIntEnum):
    Default = 0
    LastReplied = 1
    MostReplied = 2
    Popularity = 3
    Controversiality = 4
    Liked = 5
    HighestRated = 6
    MostUpvoted = 7


class ForumThreadSortEnum(DocumentedIntEnum):
    Newest = 0
    Oldest = 1


class CommunityContentSortMode(DocumentedIntEnum):
    Trending = 0
    Latest = 1
    HighestRated = 2


class ForumMediaType(DocumentedIntEnum):
    None_ = 0
    Image = 1
    Video = 2
    Youtube = 3


class ForumPostCategoryEnums(DocumentedIntFlag):
    None_ = 0
    TextOnly = 1
    Media = 2
    Link = 4
    Poll = 8
    Question = 16
    Answered = 32
    Announcement = 64
    ContentComment = 128
    BungieOfficial = 256
    NinjaOfficial: 512
    Recruitment: 1024


class ForumFlagsEnum(DocumentedIntFlag):
    None_ = 0
    BungieStaffPost = 1
    ForumNinjaPost = 2
    ForumMentorPost = 4
    TopicBungieStaffPosted = 8
    TopicBungieVolunteerPosted = 16
    QuestionAnsweredByBungie = 32
    QuestionAnsweredByNinja = 64
    CommunityContent = 128


class ForumPostPopularity(DocumentedIntEnum):
    Empty = 0
    Default = 1
    Discussed = 2
    CoolStory = 3
    HeatingUp = 4
    Hot = 5


class ForumRecruitmentIntensityLabel(DocumentedIntEnum):
    None_ = 0
    Casual = 1
    Professional = 2


class ForumRecruitmentToneLabel(DocumentedIntEnum):
    None_ = 0
    FamilyFriendly = 1
    Rowdy = 2


class ForumPostSortEnum(DocumentedIntEnum):
    Default = 0
    OldestFirst = 1
