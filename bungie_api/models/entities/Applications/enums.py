from ..framework import DocumentedIntEnum, DocumentedIntFlag


__all__ = [
    'ApplicationScopes',
    'ApplicationStatus',
    'DeveloperRole',
]


# ==================
#       Enums
# ==================
class ApplicationScopes(DocumentedIntFlag):
    None_ = -1, 'No scope given.'
    ReadBasicUserProfile = 1, (
        'Read basic user profile information such as the user\'s handle, avatar icon, etc.'
    )
    ReadGroups = 2, (
        'Read Group/Clan Forums, Wall, and Members for groups and clans that the user has joined.'
    )
    WriteGroups = 4, (
        'Write Group/Clan Forums, Wall, and Members for groups and clans that the user has joined.'
    )
    AdminGroups = 8, (
        'Administer Group/Clan Forums, Wall, and Members for groups and clans that the user is a founder or an '
        'administrator.'
    )
    BnetWrite = 16, (
        'Create new groups, clans, and forum posts, along with other actions that are reserved for Bungie.net elevated '
        'scope: not meant to be used by third party applications.'
    )
    MoveEquipDestinyItems = 32, (
        'Move or equip Destiny items.'
    )
    ReadDestinyInventoryAndVault = 64, (
        'Read Destiny 1 Inventory and Vault contents. For Destiny 2, this scope is needed to read anything regarded as '
        'private. This is the only scope a Destiny 2 app needs for read operations against Destiny 2 data such as '
        'inventory, vault, currency, vendors, milestones, progression, etc.'
    )
    ReadUserData = 128, (
        'Read user data such as who they are web notifications, clan/group memberships, recent activity, muted users.'
    )
    EditUserData = 256, (
        'Edit user data such as preferred language, status, motto, avatar selection and theme.'
    )
    ReadDestinyVendorsAndAdvisors = 512, (
        'Access vendor and advisor data specific to a user. OBSOLETE. This scope is only used on the Destiny 1 API.'
    )
    ReadAndApplyTokens = 1024, (
        'Read offer history and claim and apply tokens for the user.'
    )
    AdvancedWriteActions = 2048, (
        'Can perform actions that will result in a prompt to the user via the Destiny app.'
    )
    PartnerOfferGrant = 4096, (
        'Can user the partner offer api to claim rewards defined for a partner.'
    )
    DestinyUnlockValueQuery = 8192, (
        'Allows an app to query sensitive information like unlock flags and values not available through normal '
        'methods.'
    )
    UserPiiRead = 16384, (
        'Allows an app to query sensitive user PII, most notably email information.'
    )


class ApplicationStatus(DocumentedIntEnum):
    None_ = 0, 'No value assigned.'
    Private = 1, (
        'Application exists and works but will not appear in any public catalog. '
        'New applications start in this state, test applications will remain in this state.'
    )
    Public = 2, 'Active applications that can appear in an catalog.'
    Disabled = 3, (
        'Application disabled by the owner. All authorizations will be treated as terminated while in this state. '
        'Owner can move back to private or public state.'
    )
    Blocked = 4, (
        'Application has been blocked by Bungie. It cannot be transitioned out of this state by the owner. '
        'Authorizations are terminated when an application is in this state.'
    )


class DeveloperRole(DocumentedIntEnum):
    None_ = 0
    Owner = 1
    TeamMember = 2
