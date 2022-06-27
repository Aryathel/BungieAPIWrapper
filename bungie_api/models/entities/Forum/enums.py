from ..framework import DocumentedIntEnum, DocumentedIntFlag


__all__ = [
    'ForumTopicsCategoryFiltersEnum',
    'ForumTopicsQuickDateEnum',
    'ForumTopicsSortEnum',
    'ForumThreadSortEnum',
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
