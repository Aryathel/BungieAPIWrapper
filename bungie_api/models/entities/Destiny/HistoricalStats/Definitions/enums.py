from ....framework import DocumentedIntEnum


__all__ = [
    'DestinyActivityModeType',
    'PeriodType',
    'DestinyStatsCategoryType',
    'UnitType',
    'DestinyStatsMergeMethod',
    'DestinyStatsGroupType',
]


class DestinyActivityModeType(DocumentedIntEnum):
    None_ = 0
    Story = 2
    Strike = 3
    Raid = 4
    AllPvP = 5
    Patrol = 6
    AllPvE = 7
    Reserved9 = 9
    Control = 10
    Reserved11 = 11
    Clash = 12
    Reserved13 = 13
    CrimsonDoubles = 15
    Nightfall = 16
    HeroicNightfall = 17
    AllStrikes = 18
    IronBanner = 19
    Reserved20 = 20
    Reserved21 = 21
    Reserved22 = 22
    Reserved24 = 24
    AllMayhem = 25
    Reserved26 = 26
    Reserved27 = 27
    Reserved28 = 28
    Reserved29 = 29
    Reserved30 = 30
    Supremacy = 31
    PrivateMatchesAll = 32
    Survival = 37
    Countdown = 38
    TrialsOfTheNine = 39
    Social = 40
    TrialsCountdown = 41
    TrialsSurvival = 42
    IconBannerControl = 43
    IconBannerClash = 44
    IronBannerSupremacy = 45
    ScoredNightfall = 46
    ScoredHeroicNightfall = 47
    Rumble = 48
    AllDoubles = 49
    Doubles = 50
    PrivateMatchesClash = 51
    PrivateMatchesControl = 52
    PrivateMatchesSupremacy = 53
    PrivateMatchesCountdown = 54
    PrivateMatchesSurvival = 55
    PrivateMatchesMayhem = 56
    PrivateMatchesRumble = 57
    HeroicAdventure = 58
    Showdown = 59
    Lockdown = 60
    Scorched = 61
    ScorchedTeam = 62
    Gambit = 63
    AllPvECompetitive = 64
    Breakthrough = 65
    BlackArmoryRun = 66
    Salvage = 67
    IronBannerSalvage = 68
    PvPCompetitive = 69
    PvPQuickplay = 70
    ClashQuickplay = 71
    ClashCompetitive = 72
    ControlQuickplay = 73
    ControlCompetitive = 74
    GambitPrime = 75
    Reckoning = 76
    Menagerie = 77
    VexOffensive = 78
    NightmareHunt = 79
    Elimination = 80
    Momentum = 81
    Dungeon = 82
    Sundial = 83
    TrialsOfOsiris = 84
    Dares = 85
    Offensive = 86
    LostSector = 87
    Rift = 88
    ZoneControl = 89
    IronBannerRift = 90


class PeriodType(DocumentedIntEnum):
    None_ = 0
    Daily = 1
    AllTime = 2
    Activity = 3


class DestinyStatsCategoryType(DocumentedIntEnum):
    None_ = 0
    Kills = 1
    Assists = 2
    Deaths = 3
    Criticals = 4
    KDa = 5
    KD = 6
    Score = 7
    Entered = 8
    TimePlayed = 9
    MedalWins = 10
    MedalGame = 11
    MedalSpecialKills = 12
    MedalSprees = 13
    MedalMultiKills = 14
    MedalAbilities = 15


class UnitType(DocumentedIntEnum):
    None_ = 0
    Count = 1, 'Indicates the statistic is a simple count of something.'
    PerGame = 2, 'Indicates the statistic is a per game average.'
    Seconds = 3, 'Indicates the number of seconds'
    Points = 4, 'Indicates the number of points earned'
    Team = 5, 'Values represents a team ID'
    Distance = 6, 'Values represents a distance (units to-be-determined)'
    Percent = 7, 'Ratio represented as a whole value from 0 to 100.'
    Ratio = 8, 'Ratio of something, shown with decimal places'
    Boolean = 9, 'True or False'
    WeaponType = 10, 'The stat is actually a weapon type.'
    Standing = 11, 'Indicates victory, defeat, or something in between.'
    Milliseconds = 12, 'Number of milliseconds some event spanned. For example, race time, or lap time.'
    CompletionReason = 13, 'The value is a enumeration of the Completion Reason type.'


class DestinyStatsMergeMethod(DocumentedIntEnum):
    Add = 0, 'When collapsing multiple instances of the stat together, add the values.'
    Min = 1, 'When collapsing multiple instances of the stat together, take the lower value.'
    Max = 2, 'When collapsing multiple instances of the stat together, take the higher value.'


class DestinyStatsGroupType(DocumentedIntEnum):
    None_ = 0
    General = 1
    Weapons = 2
    Medals = 3
    ReservedGroups = 100, (
        'This is purely to serve as the dividing line between filterable and un-filterable groups. Below this number '
        'is a group you can pass as a filter. Above it are groups used in very specific circumstances and not relevant '
        'for filtering.'
    )
    Leaderboard = 101, 'Only applicable while generating leaderboards.'
    Activity = 102, 'These will *only* be consumed by GetAggregateStatsByActivity'
    UniqueWeapon = 103, 'These are only consumed and returned by GetUniqueWeaponHistory'
    Internal = 104
