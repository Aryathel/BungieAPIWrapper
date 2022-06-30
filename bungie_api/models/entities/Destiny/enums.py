from ..framework import DocumentedIntEnum, DocumentedIntFlag


__all__ = [
    'DestinyScope',
    'DestinyPresentationNodeState',
    'DestinyPresentationNodeType',
    'DestinyPresentationDisplayStyle',
    'SpecialItemType',
    'DestinyItemType',
    'DestinyClass',
    'DestinyGender',
    'DestinyRace',
    'DestinyItemSubType',
    'DamageType',
    'DestinyBreakerType',
    'PlugUiStyles',
    'PlugAvailabilityMode',
    'DestinyEnergyType',
    'ItemPerkVisibility',
    'TierType',
    'DestinyRecordState',
    'DestinyRecordValueStyle',
    'DestinyRecordToastStyle',
    'DestinyGameVersions',
    'ItemBindStatus',
    'ItemLocation',
    'TransferStatuses',
    'ItemState',
    'DestinyComponentType',
    'DestinyVendorItemRefundPolicy',
    'DestinyCollectibleState',
    'DestinyPartyMemberStates',
    'DestinyGamePrivacySetting',
    'DestinyJoinClosedReasons',
    'DestinyProgressionRewardItemState',
    'DestinyActivityDifficultyTier',
    'EquipFailureReason',
    'TalentNodeState',
    'DestinyVendorFilter',
    'VendorItemStatus',
    'DestinyVendorItemState',
]


class DestinyScope(DocumentedIntEnum):
    Profile = 0
    Character = 1


class DestinyPresentationNodeState(DocumentedIntEnum):
    None_ = 0
    Invisible = 1
    Obscured = 2


class DestinyPresentationNodeType(DocumentedIntEnum):
    Default = 0
    Category = 1
    Collectibles = 2
    Records = 3
    Metric = 4
    Craftable = 5


class DestinyPresentationDisplayStyle(DocumentedIntEnum):
    Category = 0, 'Display the item as a category, through which sub-items are filtered.'
    Badge = 1
    Medals = 2
    Collectible = 3
    Record = 4


class SpecialItemType(DocumentedIntEnum):
    None_ = 0
    SpecialCurrency = 1
    Armor = 8
    Weapon = 9
    Engram = 23
    Consumable = 24
    ExchangeMaterial = 25
    MissionReward = 27
    Currency = 29


class DestinyItemType(DocumentedIntEnum):
    None_ = 0
    Currency = 1
    Armor = 2
    Weapon = 3
    Message = 7
    Engram = 8
    Consumable = 9
    ExchangeMaterial = 10
    MissionReward = 11
    QuestStep = 12
    QuestStepComplete = 13
    Emblem = 14
    Quest = 15
    Subclass = 16
    ClanBanner = 17
    Aura = 18
    Mod = 19
    Dummy = 20
    Ship = 21
    Vehicle = 22
    Emote = 23
    Chost = 24
    Package = 26
    Bounty = 26
    Wrapper = 27
    SeasonalArtifact = 28
    Finisher = 29
    Pattern = 30


class DestinyItemSubType(DocumentedIntEnum):
    None_ = 0
    Crucible = 1, 'DEPRECATED. Items can be both "Crucible" and something else interesting.'
    Vanguard = 2, 'DEPRECATED. An item can both be "Vanguard" and something else.'
    Exotic = 5, 'DEPRECATED. An item can both be Exotic and something else.'
    AutoRifle = 6
    Shotgun = 7
    Machinegun = 8
    HandCannon = 9
    RocketLauncher = 10
    FusionRifle = 11
    SniperRifles = 12
    PulseRifle = 13
    ScoutRifle = 14
    Crm = 15, 'DEPRECATED. An item can both be CRM and something else.'
    Sidearm = 17
    Sword = 18
    Mask = 19
    Shader = 20
    Ornament = 21
    FusionRifleLine = 22
    GrenadeLauncher = 23
    SubmachineGun = 24
    TraceRifle = 25
    HelmetArmor = 26
    GauntletsArmor = 27
    ChestArmor = 28
    LegArmor = 29
    ClassArmor = 30
    Bow = 31
    DummyRepeatableBounty = 32
    Glaive = 33


class DestinyClass(DocumentedIntEnum):
    Titan = 0
    Hunter = 1
    Warlock = 2
    Unknown = 3


class DestinyGender(DocumentedIntEnum):
    Male = 0
    Female = 1
    Unknown = 2


class DestinyRace(DocumentedIntEnum):
    Human = 0
    Awoken = 1
    Exo = 2
    Unknown = 3


class DamageType(DocumentedIntEnum):
    None_ = 0
    Kinetic = 1
    Arc = 2
    Thermal = 3
    Void = 4
    Raid = 5
    Stasis = 6


class DestinyBreakerType(DocumentedIntEnum):
    None_ = 0
    ShieldPiercing = 1
    Disruption = 2
    Stagger = 3


class PlugUiStyles(DocumentedIntEnum):
    None_ = 0
    Masterwork = 1


class PlugAvailabilityMode(DocumentedIntEnum):
    Normal = 0
    UnavailableIfSocketContainsMatchingPlugCategory = 1
    AvailableIfSocketContainsMatchingPlugCategory = 2


class DestinyEnergyType(DocumentedIntEnum):
    Any = 0
    Arc = 1
    Thermal = 2
    Void = 3
    Ghost = 4
    Subclass = 5
    Stasis = 6


class ItemPerkVisibility(DocumentedIntEnum):
    Visible = 0
    Disabled = 1
    Hidden = 2


class TierType(DocumentedIntEnum):
    Unknown = 0
    Currency = 1
    Basic = 2
    Common = 3
    Rare = 4
    Superior = 5
    Exotic = 6


class DestinyRecordState(DocumentedIntFlag):
    None_ = 0, (
        'If there are no flags set, the record is in a state where it *could* be redeemed, but it has not been yet.'
    )
    RecordRedeemed = 1, 'If this is set, the completed record has been redeemed.'
    RewardUnavailable = 2, (
        'If this is set, there\'s a reward available from this Record but it\'s unavailable for redemption.'
    )
    ObjectiveNotCompleted = 4, 'If this is set, the objective for this Record has not yet been completed.'
    Obscured = 8, (
        'If this is set, the game recommends that you replace the display text of this Record with '
        'DestinyRecordDefinition.stateInfo.obscuredString.'
    )
    Invisible = 16, (
        'If this is set, the game recommends that you not show this record. Do what you will with this recommendation.'
    )
    EntitlementUnowned = 32, (
        'If this is set, you can\'t complete this record because you lack some permission that\'s required to complete '
        'it.'
    )
    CanEquipTitle = 64, (
        'If this is set, the record has a title (check DestinyRecordDefinition for title info) and you can equip it.'
    )


class DestinyRecordValueStyle(DocumentedIntEnum):
    Integer = 0
    Percentage = 1
    Milliseconds = 2
    Boolean = 3
    Decimal = 4


class DestinyRecordToastStyle(DocumentedIntEnum):
    None_ = 0
    Record = 1
    Lore = 2
    Badge = 3
    MetaRecord = 4
    MedalComplete = 5
    SeasonChallengeComplete = 6
    GildedTitleComplete = 7
    CraftingRecipeUnlocked = 8


class DestinyGameVersions(DocumentedIntFlag):
    None_ = 0
    Destiny2 = 1
    DLC1 = 2
    DLC2 = 4
    Forsaken = 8
    YearTwoAnnualPass = 16
    Shadowkeep = 32
    BeyondLight = 64
    Anniversary30th = 128
    TheWitchQueen = 256


class ItemBindStatus(DocumentedIntEnum):
    NotBound = 0
    BoundToCharacter = 1
    BoundToAccount = 2
    BoundToGuild = 3


class ItemLocation(DocumentedIntEnum):
    Unknown = 0
    Inventory = 1
    Vault = 2
    Vendor = 3
    Postmaster = 4


class TransferStatuses(DocumentedIntFlag):
    CanTransfer = 0, 'The item can be transferred.'
    ItemIsEquipped = 1, 'You can\'t transfer the item because it is equipped on a character.'
    NotTransferrable = 2, (
        'The item is defined as not transferrable in its DestinyInventoryItemDefinition.nonTransferrable property.'
    )
    NoRoomInDestination = 4, (
        'You could transfer the item, but the place you\'re trying to put it has run out of room! Check your remaining '
        'Vault and/or character space.'
    )


class ItemState(DocumentedIntFlag):
    None_ = 0
    Locked = 1, (
        'If this bit is set, the item has been "locked" by the user and cannot be deleted. You may want to represent '
        'this visually with a "lock" icon.'
    )
    Tracked = 2, (
        'If this bit is set, the item is a quest that\'s being tracked by the user. You may want a visual indicator '
        'to show that this is a tracked quest.'
    )
    Masterwork = 4, (
        'If this bit is set, the item has a Masterwork plug inserted. This usually coincides with having a special '
        '"glowing" effect applied to the item\'s icon.'
    )
    Crafted = 8, (
        'If this bit is set, the item has been \'crafted\' by the player. You may want to represent this visually with '
        'a "crafted" icon overlay.'
    )
    HighlightedObjective = 16, (
        'If this bit is set, the item has a \'highlighted\' objective. You may want to represent this with an '
        'orange-red icon border color.'
    )


class DestinyComponentType(DocumentedIntEnum):
    None_ = 0
    Profiles = 100, (
        'Profiles is the most basic component, only relevant when calling GetProfile. This returns basic information '
        'about the profile, which is almost nothing: a list of characterIds, some information about the last time you '
        'logged in, and that most sobering statistic: how long you\'ve played.'
    )
    VendorReceipts = 101, (
        'Only applicable for GetProfile, this will return information about receipts for refundable vendor items.'
    )
    ProfileInventories = 102, (
        'Asking for this will get you the profile-level inventories, such as your Vault buckets (yeah, the Vault is '
        'really inventory buckets located on your Profile)'
    )
    ProfileCurrencies = 103, (
        'This will get you a summary of items on your Profile that we consider to be "currencies", such as Glimmer. I '
        'mean, if there\'s Glimmer in Destiny 2. I didn\'t say there was Glimmer.'
    )
    ProfileProgression = 104, (
        'This will get you any progression-related information that exists on a Profile-wide level, across all '
        'characters.'
    )
    PlatformSilver = 105, (
        'This will get you information about the silver that this profile has on every platform on which it plays.\n\n'
        'You may only request this component for the logged in user\'s Profile, and will not receive it if you request '
        'it for another Profile.'
    )

    Characters = 200, (
        'This will get you summary info about each of the characters in the profile.'
    )
    CharacterInventories = 201, (
        'This will get you information about any non-equipped items on the character or character(s) in question, if '
        'you\'re allowed to see it. You have to either be authenticated as that user, or that user must allow '
        'anonymous viewing of their non-equipped items in Bungie.Net settings to actually get results.'
    )
    CharacterProgressions = 202, (
        'This will get you information about the progression (faction, experience, etc... "levels") relevant to each '
        'character, if you are the currently authenticated user or the user has elected to allow anonymous viewing of '
        'its progression info.'
    )
    CharacterRenderData = 203, (
        'This will get you just enough information to be able to render the character in 3D if you have written a 3D '
        'rendering library for Destiny Characters, or "borrowed" ours. It\'s okay, I won\'t tell anyone if you\'re '
        'using it. I\'m no snitch. (actually, we don\'t care if you use it - go to town)'
    )
    CharacterActivities = 204, (
        'This will return info about activities that a user can see and gating on it, if you are the currently '
        'authenticated user or the user has elected to allow anonymous viewing of its progression info. Note that the '
        'data returned by this can be unfortunately problematic and relatively unreliable in some cases. We\'ll '
        'eventually work on making it more consistently reliable.'
    )
    CharacterEquipment = 205, (
        'This will return info about the equipped items on the character(s). Everyone can see this.'
    )

    ItemInstances = 300, (
        'This will return basic info about instanced items - whether they can be equipped, their tracked status, and '
        'some info commonly needed in many places (current damage type, primary stat value, etc)'
    )
    ItemObjectives = 301, (
        'Items can have Objectives (DestinyObjectiveDefinition) bound to them. If they do, this will return info for '
        'items that have such bound objectives.'
    )
    ItemPerks = 302, (
        'Items can have perks (DestinyPerkDefinition). If they do, this will return info for what perks are active on '
        'items.'
    )
    ItemRenderData = 303, (
        'If you just want to render the weapon, this is just enough info to do that rendering.'
    )
    ItemStats = 304, (
        'Items can have stats, like rate of fire. Asking for this component will return requested item\'s stats if '
        'they have stats.'
    )
    ItemSockets = 305, (
        'Items can have sockets, where plugs can be inserted. Asking for this component will return all info relevant '
        'to the sockets on items that have them.'
    )
    ItemTalentGrids = 306, (
        'Items can have talent grids, though that matters a lot less frequently than it used to. Asking for this '
        'component will return all relevant info about activated Nodes and Steps on this talent grid, like the good '
        'ol\' days.'
    )
    ItemCommonData = 307, (
        'Items that *aren\'t* instanced still have important information you need to know: how much of it you have, '
        'the itemHash so you can look up their DestinyInventoryItemDefinition, whether they\'re locked, etc... Both '
        'instanced and non-instanced items will have these properties. You will get this automatically with '
        'Inventory components - you only need to pass this when calling GetItem on a specific item.'
    )
    ItemPlugStates = 308, (
        'Items that are "Plugs" can be inserted into sockets. This returns statuses about those plugs and why they '
        'can/can\'t be inserted. I hear you giggling, there\'s nothing funny about inserting plugs. Get your head out '
        'of the gutter and pay attention!'
    )
    ItemPlugObjectives = 309, (
        'Sometimes, plugs have objectives on them. This data can get really large, so we split it into its own '
        'component. Please, don\'t grab it unless you need it.'
    )
    ItemReusabledPlugs = 310, (
        'Sometimes, designers create thousands of reusable plugs and suddenly your response sizes are almost 3MB, and '
        'something has to give.\n\nReusable Plugs were split off as their own component, away from ItemSockets, as a '
        'result of the Plug changes in Shadowkeep that made plug data infeasibly large for the most common use cases.'
        '\n\nRequest this component if and only if you need to know what plugs *could* be inserted into a socket, and '
        'need to know it before "drilling" into the details of an item in your application (for instance, if you\'re '
        'doing some sort of interesting sorting or aggregation based on available plugs.\n\nWhen you get this, you '
        'will also need to combine it with "Plug Sets" data if you want a full picture of all of the available plugs: '
        'this component will only return plugs that have state data that is per-item. See Plug Sets for available '
        'plugs that have Character, Profile, or no state-specific restrictions.'
    )

    Vendors = 400, (
        'When obtaining vendor information, this will return summary information about the Vendor or Vendors being '
        'returned.'
    )
    VendorCategories = 401, (
        'When obtaining vendor information, this will return information about the categories of items provided by the '
        'Vendor.'
    )
    VendorSales = 402, (
        'When obtaining vendor information, this will return the information about items being sold by the Vendor.'
    )

    Kiosks = 500, (
        'Asking for this component will return you the account\'s Kiosk statuses: that is, what items have been filled '
        'out/acquired. But only if you are the currently authenticated user or the user has elected to allow anonymous '
        'viewing of its progression info.'
    )

    CurrencyLookups = 600, (
        'A "shortcut" component that will give you all of the item hashes/quantities of items that the requested '
        'character can use to determine if an action (purchasing, socket insertion) has the required currency. '
        '(recall that all currencies are just items, and that some vendor purchases require items that you might not '
        'traditionally consider to be a "currency", like plugs/mods!)'
    )

    PresentationNodes = 700, (
        'Returns summary status information about all "Presentation Nodes". See DestinyPresentationNodeDefinition for '
        'more details, but the gist is that these are entities used by the game UI to bucket Collectibles and Records '
        'into a hierarchy of categories. You may ask for and use this data if you want to perform similar bucketing in '
        'your own UI: or you can skip it and roll your own.'
    )

    Collectibles = 800, (
        'Returns summary status information about all "Collectibles". These are records of what items you\'ve '
        'discovered while playing Destiny, and some other basic information. For detailed information, you will have '
        'to call a separate endpoint devoted to the purpose.'
    )

    Records = 900, (
        'Returns summary status information about all "Records" (also known in the game as "Triumphs". I know, it\'s '
        'confusing because there\'s also "Moments of Triumph" that will themselves be represented as "Triumphs.")'
    )

    Transitory = 1000, (
        'Returns information that Bungie considers to be "Transitory": data that may change too frequently or come '
        'from a non-authoritative source such that we don\'t consider the data to be fully trustworthy, but that might '
        'prove useful for some limited use cases. We can provide no guarantee of timeliness nor consistency for this '
        'data: buyer beware with the Transitory component.'
    )

    Metrics = 1100, (
        'Returns summary status information about all "Metrics" (also known in the game as "Stat Trackers").'
    )

    StringVariables = 1200, (
        'Returns a mapping of localized string variable hashes to values, on a per-account or per-character basis.'
    )

    Craftables = 1300, (
        'Returns summary status information about all "Craftables" aka crafting recipe items.'
    )


class DestinyVendorItemRefundPolicy(DocumentedIntEnum):
    NotRefundable = 0
    DeletesItem = 1
    RevokesLicense = 2


class DestinyCollectibleState(DocumentedIntFlag):
    None_ = 0
    NotAcquired = 1, 'If this flag is set, you have not yet obtained this collectible.'
    Obscured = 2, (
        'If this flag is set, the item is "obscured" to you: you can/should use the alternate item hash found in '
        'DestinyCollectibleDefinition.stateInfo.obscuredOverrideItemHash when displaying this collectible instead of '
        'the default display info.'
    )
    Invisible = 4, (
        'If this flag is set, the collectible should not be shown to the user.\n\nPlease do consider honoring this '
        'flag. It is used - for example - to hide items that a person didn\'t get from the Eververse. I can\'t prevent '
        'these from being returned in definitions, because some people may have acquired them and thus they should show '
        'up: but I would hate for people to start feeling some variant of a Collector\'s Remorse about these items, '
        'and thus increasing their purchasing based on that compulsion. That would be a very unfortunate outcome, and '
        'one that I wouldn\'t like to see happen. So please, whether or not I\'m your mom, consider honoring this flag '
        'and don\'t show people invisible collectibles.'
    )
    CannotAffordMaterialRequirements = 8, (
        'If this flag is set, the collectible requires payment for creating an instance of the item, and you are '
        'lacking in currency. Bring the benjamins next time. Or spinmetal. Whatever.'
    )
    InventorySpaceUnavailable = 16, (
        'If this flag is set, you can\'t pull this item out of your collection because there\'s no room left in your '
        'inventory.'
    )
    UniquenessViolation = 32, 'If this flag is set, you already have one of these items and can\'t have a second one.'
    PurchaseDisabled = 64, (
        'If this flag is set, the ability to pull this item out of your collection has been disabled.'
    )


class DestinyPartyMemberStates(DocumentedIntFlag):
    None_ = 0
    FireteamMember = 1, 'This one\'s pretty obvious - they\'re on your Fireteam.'
    PosseMember = 2, 'I don\'t know what it means to be in a \'Posse\', but apparently this is it.'
    GroupMember = 4, (
        'Nor do I understand the difference between them being in a \'Group\' vs. a \'Fireteam\'.\n\nI\'ll update '
        'these docs once I get more info. If I get more info. If you\'re reading this, I never got more info. You\'re '
        'on your own, kid.'
    )
    PartyLeader = 8, 'This person is the party leader.'


class DestinyGamePrivacySetting(DocumentedIntEnum):
    Open = 0
    ClanAndFriendsOnly = 1
    FriendsOnly = 2
    InvitationOnly = 3
    Closed = 4


class DestinyJoinClosedReasons(DocumentedIntFlag):
    None_ = 0
    InMatchmaking = 1, 'The user is currently in matchmaking.'
    Loading = 2, 'The user is currently in a loading screen.'
    SoloMode = 4, 'The user is in an activity that requires solo play.'
    InternalResources = 8, (
        'The user can\'t be joined for one of a variety of internal reasons. Basically, the game can\'t let you join '
        'at this time, but for reasons that aren\'t under the control of this user.'
    )
    DisallowedByGameState = 16, 'The user\'s current activity/quest/other transitory game state is preventing joining.'
    Offline = 32768, 'The user appears to be offline.'


class DestinyProgressionRewardItemState(DocumentedIntFlag):
    None_ = 0
    Invisible = 1, 'If this is set, the reward should be hidden.'
    Earned = 2, 'If this is set, the reward has been earned.'
    Claimed = 4, 'If this is set, the reward has been claimed.'
    ClaimAllowed = 8, (
        'If this is set, the reward is allowed to be claimed by this Character. An item can be earned but still can\'t '
        'be claimed in certain circumstances, like if it\'s only allowed for certain subclasses. It also might not be '
        'able to be claimed if you already claimed it!'
    )


class DestinyActivityDifficultyTier(DocumentedIntEnum):
    Trivial = 0
    Easy = 1
    Normal = 2
    Challenging = 3
    Hard = 4
    Brave = 5
    AlmostImpossible = 6
    Impossible = 7


class EquipFailureReason(DocumentedIntFlag):
    None_ = 0, 'The item is/was able to be equipped.'
    ItemUnequippable = 1, (
        'This is not the kind of item that can be equipped. Did you try equipping Glimmer or something?'
    )
    ItemUniqueEquipRestricted = 2, (
        'This item is part of a "unique set", and you can\'t have more than one item of that same set type equipped at '
        'once. For instance, if you already have an Exotic Weapon equipped, you can\'t equip a second one in another '
        'weapon slot.'
    )
    ItemFailedUnlockCheck = 4, (
        'This item has state-based gating that prevents it from being equipped in certain circumstances. For instance, '
        'an item might be for Warlocks only and you\'re a Titan, or it might require you to have beaten some special '
        'quest that you haven\'t beaten yet. Use the additional failure data passed on the item itself to get more '
        'information about what the specific failure case was (See DestinyInventoryItemDefinition and '
        'DestinyItemInstanceComponent)'
    )
    ItemFailedLevelCheck = 8, (
        'This item requires you to have reached a specific character level in order to equip it, and you haven\'t '
        'reached that level yet.'
    )
    ItemNotOnCharacter = 16, (
        'This item can\'t be equipped on the character requested, because it must be in that character\'s inventory '
        'first. Transfer the item to the character you want to equip it before you attempt to equip it.'
    )


class TalentNodeState(DocumentedIntEnum):
    Invalid = 0
    CanUpgrade = 1
    NoPoints = 2
    NoPrerequisites = 3
    NoSteps = 4
    NoMaterial = 6
    NoGridLevel = 7
    SwappingLocked = 8
    MustSwap = 9
    Complete = 10
    Unknown = 11
    CreationOnly = 12
    Hidden = 13


class DestinyVendorFilter(DocumentedIntEnum):
    None_ = 0
    ApiPurchasable = 1


class VendorItemStatus(DocumentedIntFlag):
    Success = 0
    NoInventorySpace = 1
    NoFunds = 2
    NoProgression = 4
    NoUnlock = 8
    NoQuantity = 16
    OutsidePurchaseWindow = 32
    NotAvailable = 64
    UniquenessViolation = 128
    UnknownError = 256
    AlreadySelling = 512
    Unsellable = 1024
    SellingInhibited = 2048
    AlreadyOwned = 4096
    DisplayOnly = 8192


class DestinyVendorItemState(DocumentedIntFlag):
    None_ = 0, 'There are no augments on this item.'
    Incomplete = 1, (
        'Deprecated forever (probably). There was a time when Records were going to be implemented through Vendors, '
        'and this field was relevant. Now they\'re implemented through Presentation Nodes, and this field doesn\'t '
        'matter anymore.'
    )
    RewardAvailable = 2, (
        'Deprecated forever (probably). See the description of the "Incomplete" value for the juicy scoop.'
    )
    Complete = 4, (
        'Deprecated forever (probably). See the description of the "Incomplete" value for the juicy scoop.'
    )
    New = 8, 'This item is considered to be "newly available", and should have some UI showing how shiny it is.'
    Featured = 16, (
        'This item is being "featured", and should be shiny in a different way from items that are merely new.'
    )
    Ending = 32, 'This item is only available for a limited time, and that time is approaching.'
    OnSale = 64, 'This item is "on sale". Get it while it\'s hot.'
    Owned = 128, 'This item is already owned.'
    WideView = 256, 'This item should be shown with a "wide view" instead of normal icon view.'
    NexusAttention = 512, (
        'This indicates that you should show some kind of attention-requesting indicator on the item, in a similar '
        'manner to items in the nexus that have such notifications.'
    )
    SetDiscount = 1024, 'This indicates that the item has some sort of a \'set\' discount.'
    PriceDrop = 2048, 'This indicates that the item has a price drop.'
    DailyOffer = 4096, 'This indicates that the item is a daily offer.'
    Charity = 8192, 'This indicates that the item is for charity.'
    SeasonalRewardExpiration = 16384, 'This indicates that the item has a seasonal reward expiration.'
    BestDeal = 32768, 'This indicates that the sale item is the best deal among different choices.'
    Popular = 65536, 'This indicates that the sale item is popular.'
    Free = 131072, 'This indicates that the sale item is free.'
    Locked = 262144, 'This indicates that the sale item is locked.'
