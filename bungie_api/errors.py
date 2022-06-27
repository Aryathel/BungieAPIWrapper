__all__ = [
    'DestinyException',
    'ObsoleteError',
    'None_',
    'Success',
    'TransportException',
    'UnhandledException',
    'NotImplemented',
    'SystemDisabled',
    'FailedToLoadAvailableLocalesConfiguration',
    'ParameterParseFailure',
    'ParameterInvalidRange',
    'BadRequest',
    'AuthenticationInvalid',
    'DataNotFound',
    'InsufficientPrivileges',
    'Duplicate',
    'UnknownSqlResult',
    'ValidationError',
    'ValidationMissingFieldError',
    'ValidationInvalidInputError',
    'InvalidParameters',
    'ParameterNotFound',
    'UnhandledHttpException',
    'NotFound',
    'WebAuthModuleAsyncFailed',
    'InvalidReturnValue',
    'UserBanned',
    'InvalidPostBody',
    'MissingPostBody',
    'ExternalServiceTimeout',
    'ValidationLengthError',
    'ValidationRangeError',
    'JsonDeserializationError',
    'ThrottleLimitExceeded',
    'ValidationTagError',
    'ValidationProfanityError',
    'ValidationUrlFormatError',
    'ThrottleLimitExceededMinutes',
    'ThrottleLimitExceededMomentarily',
    'ThrottleLimitExceededSeconds',
    'ExternalServiceUnknown',
    'ValidationWordLengthError',
    'ValidationInvisibleUnicode',
    'ValidationBadNames',
    'ExternalServiceFailed',
    'ServiceRetired',
    'UnknownSqlException',
    'UnsupportedLocale',
    'InvalidPageNumber',
    'MaximumPageSizeExceeded',
    'ServiceUnsupported',
    'ValidationMaximumUnicodeCombiningCharacters',
    'ValidationMaximumSequentialCarriageReturns',
    'PerEndpointRequestThrottleExceeded',
    'AuthContextCacheAssertion',
    'ExPlatformStringValidationError',
    'PerApplicationThrottleExceeded',
    'PerApplicationAnonymousThrottleExceeded',
    'PerApplicationAuthenticatedThrottleExceeded',
    'PerUserThrottleExceeded',
    'PayloadSignatureVerificationFailure',
    'InvalidServiceAuthContext',
    'ObsoleteCredentialType',
    'UnableToUnPairMobileApp',
    'UnableToPairMobileApp',
    'CannotUseMobileAuthWithNonMobileProvider',
    'MissingDeviceCookie',
    'FacebookTokenExpired',
    'AuthTicketRequired',
    'CookieContextRequired',
    'UnknownAuthenticationError',
    'BungieNetAccountCreationRequired',
    'WebAuthRequired',
    'ContentUnknownSqlResult',
    'ContentNeedUniquePath',
    'ContentSqlException',
    'ContentNotFound',
    'ContentSuccessWithTagAddFail',
    'ContentSearchMissingParameters',
    'ContentInvalidId',
    'ContentPhysicalFileDeletionError',
    'ContentPhysicalFileCreationError',
    'ContentPerforceSubmissionError',
    'ContentPerforceInitializationError',
    'ContentDeploymentPackageNotReadyError',
    'ContentUploadFailed',
    'ContentTooManyResults',
    'ContentInvalidState',
    'ContentNavigationParentNotFound',
    'ContentNavigationParentUpdateError',
    'DeploymentPackageNotEditable',
    'ContentValidationError',
    'ContentPropertiesValidationError',
    'ContentTypeNotFound',
    'DeploymentPackageNotFound',
    'ContentSearchInvalidParameters',
    'ContentItemPropertyAggregationError',
    'DeploymentPackageFileNotFound',
    'ContentPerforceFileHistoryNotFound',
    'ContentAssetZipCreationFailure',
    'ContentAssetZipCreationBusy',
    'ContentProjectNotFound',
    'ContentFolderNotFound',
    'ContentPackagesInconsistent',
    'ContentPackagesInvalidState',
    'ContentPackagesInconsistentType',
    'ContentCannotDeletePackage',
    'ContentLockedForChanges',
    'ContentFileUploadFailed',
    'ContentNotReviewed',
    'ContentPermissionDenied',
    'ContentInvalidExternalUrl',
    'ContentExternalFileCannotBeImportedLocally',
    'ContentTagSaveFailure',
    'ContentPerforceUnmatchedFileError',
    'ContentPerforceChangelistResultNotFound',
    'ContentPerforceChangelistFileItemsNotFound',
    'ContentPerforceInvalidRevisionError',
    'ContentUnloadedSaveResult',
    'ContentPropertyInvalidNumber',
    'ContentPropertyInvalidUrl',
    'ContentPropertyInvalidDate',
    'ContentPropertyInvalidSet',
    'ContentPropertyCannotDeserialize',
    'ContentRegexValidationFailOnProperty',
    'ContentMaxLengthFailOnProperty',
    'ContentPropertyUnexpectedDeserializationError',
    'ContentPropertyRequired',
    'ContentCannotCreateFile',
    'ContentInvalidMigrationFile',
    'ContentMigrationAlteringProcessedItem',
    'ContentPropertyDefinitionNotFound',
    'ContentReviewDataChanged',
    'ContentRollbackRevisionNotInPackage',
    'ContentItemNotBasedOnLatestRevision',
    'ContentUnauthorized',
    'ContentCannotCreateDeploymentPackage',
    'ContentUserNotFound',
    'ContentLocalePermissionDenied',
    'ContentInvalidLinkToInternalEnvironment',
    'ContentInvalidBlacklistedContent',
    'ContentMacroMalformedNoContentId',
    'ContentMacroMalformedNoTemplateType',
    'ContentIllegalBNetMembershipId',
    'ContentLocaleDidNotMatchExpected',
    'ContentBabelCallFailed',
    'ContentEnglishPostLiveForbidden',
    'ContentLocaleEditPermissionDenied',
    'UserNonUniqueName',
    'UserManualLinkingStepRequired',
    'UserCreateUnknownSqlResult',
    'UserCreateUnknownSqlException',
    'UserMalformedMembershipId',
    'UserCannotFindRequestedUser',
    'UserCannotLoadAccountCredentialLinkInfo',
    'UserInvalidMobileAppType',
    'UserMissingMobilePairingInfo',
    'UserCannotGenerateMobileKeyWhileUsingMobileCredential',
    'UserGenerateMobileKeyExistingSlotCollision',
    'UserDisplayNameMissingOrInvalid',
    'UserCannotLoadAccountProfileData',
    'UserCannotSaveUserProfileData',
    'UserEmailMissingOrInvalid',
    'UserTermsOfUseRequired',
    'UserCannotCreateNewAccountWhileLoggedIn',
    'UserCannotResolveCentralAccount',
    'UserInvalidAvatar',
    'UserMissingCreatedUserResult',
    'UserCannotChangeUniqueNameYet',
    'UserCannotChangeDisplayNameYet',
    'UserCannotChangeEmail',
    'UserUniqueNameMustStartWithLetter',
    'UserNoLinkedAccountsSupportFriendListings',
    'UserAcknowledgmentTableFull',
    'UserCreationDestinyMembershipRequired',
    'UserFriendsTokenNeedsRefresh',
    'UserEmailValidationUnknown',
    'UserEmailValidationLimit',
    'TransactionEmailSendFailure',
    'MailHookPermissionFailure',
    'MailServiceRateLimit',
    'UserEmailMustBeVerified',
    'UserMustAllowCustomerServiceEmails',
    'NonTransactionalEmailSendFailure',
    'UnknownErrorSettingGlobalDisplayName',
    'DuplicateGlobalDisplayName',
    'ErrorRunningNameValidationChecks',
    'ErrorDatabaseGlobalName',
    'ErrorNoAvailableNameChanges',
    'ErrorNameAlreadySetToInput',
    'MessagingUnknownError',
    'MessagingSelfError',
    'MessagingSendThrottle',
    'MessagingNoBody',
    'MessagingTooManyUsers',
    'MessagingCanNotLeaveConversation',
    'MessagingUnableToSend',
    'MessagingDeletedUserForbidden',
    'MessagingCannotDeleteExternalConversation',
    'MessagingGroupChatDisabled',
    'MessagingMustIncludeSelfInPrivateMessage',
    'MessagingSenderIsBanned',
    'MessagingGroupOptionalChatExceededMaximum',
    'PrivateMessagingRequiresDestinyMembership',
    'AddSurveyAnswersUnknownSqlException',
    'ForumBodyCannotBeEmpty',
    'ForumSubjectCannotBeEmptyOnTopicPost',
    'ForumCannotLocateParentPost',
    'ForumThreadLockedForReplies',
    'ForumUnknownSqlResultDuringCreatePost',
    'ForumUnknownTagCreationError',
    'ForumUnknownSqlResultDuringTagItem',
    'ForumUnknownExceptionCreatePost',
    'ForumQuestionMustBeTopicPost',
    'ForumExceptionDuringTagSearch',
    'ForumExceptionDuringTopicRetrieval',
    'ForumAliasedTagError',
    'ForumCannotLocateThread',
    'ForumUnknownExceptionEditPost',
    'ForumCannotLocatePost',
    'ForumUnknownExceptionGetOrCreateTags',
    'ForumEditPermissionDenied',
    'ForumUnknownSqlResultDuringTagIdRetrieval',
    'ForumCannotGetRating',
    'ForumUnknownExceptionGetRating',
    'ForumRatingsAccessError',
    'ForumRelatedPostAccessError',
    'ForumLatestReplyAccessError',
    'ForumUserStatusAccessError',
    'ForumAuthorAccessError',
    'ForumGroupAccessError',
    'ForumUrlExpectedButMissing',
    'ForumRepliesCannotBeEmpty',
    'ForumRepliesCannotBeInDifferentGroups',
    'ForumSubTopicCannotBeCreatedAtThisThreadLevel',
    'ForumCannotCreateContentTopic',
    'ForumTopicDoesNotExist',
    'ForumContentCommentsNotAllowed',
    'ForumUnknownSqlResultDuringEditPost',
    'ForumUnknownSqlResultDuringGetPost',
    'ForumPostValidationBadUrl',
    'ForumBodyTooLong',
    'ForumSubjectTooLong',
    'ForumAnnouncementNotAllowed',
    'ForumCannotShareOwnPost',
    'ForumEditNoOp',
    'ForumUnknownDatabaseErrorDuringGetPost',
    'ForumExceeedMaximumRowLimit',
    'ForumCannotSharePrivatePost',
    'ForumCannotCrossPostBetweenGroups',
    'ForumIncompatibleCategories',
    'ForumCannotUseTheseCategoriesOnNonTopicPost',
    'ForumCanOnlyDeleteTopics',
    'ForumDeleteSqlException',
    'ForumDeleteSqlUnknownResult',
    'ForumTooManyTags',
    'ForumCanOnlyRateTopics',
    'ForumBannedPostsCannotBeEdited',
    'ForumThreadRootIsBanned',
    'ForumCannotUseOfficialTagCategoryAsTag',
    'ForumAnswerCannotBeMadeOnCreatePost',
    'ForumAnswerCannotBeMadeOnEditPost',
    'ForumAnswerPostIdIsNotADirectReplyOfQuestion',
    'ForumAnswerTopicIdIsNotAQuestion',
    'ForumUnknownExceptionDuringMarkAnswer',
    'ForumUnknownSqlResultDuringMarkAnswer',
    'ForumCannotRateYourOwnPosts',
    'ForumPollsMustBeTheFirstPostInTopic',
    'ForumInvalidPollInput',
    'ForumGroupAdminEditNonMember',
    'ForumCannotEditModeratorEditedPost',
    'ForumRequiresDestinyMembership',
    'ForumUnexpectedError',
    'ForumAgeLock',
    'ForumMaxPages',
    'ForumMaxPagesOldestFirst',
    'ForumCannotApplyForumIdWithoutTags',
    'ForumCannotApplyForumIdToNonTopics',
    'ForumCannotDownvoteCommunityCreations',
    'ForumTopicsMustHaveOfficialCategory',
    'ForumRecruitmentTopicMalformed',
    'ForumRecruitmentTopicNotFound',
    'ForumRecruitmentTopicNoSlotsRemaining',
    'ForumRecruitmentTopicKickBan',
    'ForumRecruitmentTopicRequirementsNotMet',
    'ForumRecruitmentTopicNoPlayers',
    'ForumRecruitmentApproveFailMessageBan',
    'ForumRecruitmentGlobalBan',
    'ForumUserBannedFromThisTopic',
    'ForumRecruitmentFireteamMembersOnly',
    'ForumRequiresDestiny2Progress',
    'GroupMembershipApplicationAlreadyResolved',
    'GroupMembershipAlreadyApplied',
    'GroupMembershipInsufficientPrivileges',
    'GroupIdNotReturnedFromCreation',
    'GroupSearchInvalidParameters',
    'GroupMembershipPendingApplicationNotFound',
    'GroupInvalidId',
    'GroupInvalidMembershipId',
    'GroupInvalidMembershipType',
    'GroupMissingTags',
    'GroupMembershipNotFound',
    'GroupInvalidRating',
    'GroupUserFollowingAccessError',
    'GroupUserMembershipAccessError',
    'GroupCreatorAccessError',
    'GroupAdminAccessError',
    'GroupPrivatePostNotViewable',
    'GroupMembershipNotLoggedIn',
    'GroupNotDeleted',
    'GroupUnknownErrorUndeletingGroup',
    'GroupDeleted',
    'GroupNotFound',
    'GroupMemberBanned',
    'GroupMembershipClosed',
    'GroupPrivatePostOverrideError',
    'GroupNameTaken',
    'GroupDeletionGracePeriodExpired',
    'GroupCannotCheckBanStatus',
    'GroupMaximumMembershipCountReached',
    'NoDestinyAccountForClanPlatform',
    'AlreadyRequestingMembershipForClanPlatform',
    'AlreadyClanMemberOnPlatform',
    'GroupJoinedCannotSetClanName',
    'GroupLeftCannotClearClanName',
    'GroupRelationshipRequestPending',
    'GroupRelationshipRequestBlocked',
    'GroupRelationshipRequestNotFound',
    'GroupRelationshipBlockNotFound',
    'GroupRelationshipNotFound',
    'GroupAlreadyAllied',
    'GroupAlreadyMember',
    'GroupRelationshipAlreadyExists',
    'InvalidGroupTypesForRelationshipRequest',
    'GroupAtMaximumAlliances',
    'GroupCannotSetClanOnlySettings',
    'ClanCannotSetTwoDefaultPostTypes',
    'GroupMemberInvalidMemberType',
    'GroupInvalidPlatformType',
    'GroupMemberInvalidSort',
    'GroupInvalidResolveState',
    'ClanAlreadyEnabledForPlatform',
    'ClanNotEnabledForPlatform',
    'ClanEnabledButCouldNotJoinNoAccount',
    'ClanEnabledButCouldNotJoinAlreadyMember',
    'ClanCannotJoinNoCredential',
    'NoClanMembershipForPlatform',
    'GroupToGroupFollowLimitReached',
    'ChildGroupAlreadyInAlliance',
    'OwnerGroupAlreadyInAlliance',
    'AllianceOwnerCannotJoinAlliance',
    'GroupNotInAlliance',
    'ChildGroupCannotInviteToAlliance',
    'GroupToGroupAlreadyFollowed',
    'GroupToGroupNotFollowing',
    'ClanMaximumMembershipReached',
    'ClanNameNotValid',
    'ClanNameNotValidError',
    'AllianceOwnerNotDefined',
    'AllianceChildNotDefined',
    'ClanCultureIllegalCharacters',
    'ClanTagIllegalCharacters',
    'ClanRequiresInvitation',
    'ClanMembershipClosed',
    'ClanInviteAlreadyMember',
    'GroupInviteAlreadyMember',
    'GroupJoinApprovalRequired',
    'ClanTagRequired',
    'GroupNameCannotStartOrEndWithWhiteSpace',
    'ClanCallsignCannotStartOrEndWithWhiteSpace',
    'ClanMigrationFailed',
    'ClanNotEnabledAlreadyMemberOfAnotherClan',
    'GroupModerationNotPermittedOnNonMembers',
    'ClanCreationInWorldServerFailed',
    'ClanNotFound',
    'ClanMembershipLevelDoesNotPermitThatAction',
    'ClanMemberNotFound',
    'ClanMissingMembershipApprovers',
    'ClanInWrongStateForRequestedAction',
    'ClanNameAlreadyUsed',
    'ClanTooFewMembers',
    'ClanInfoCannotBeWhitespace',
    'GroupCultureThrottle',
    'ClanTargetDisallowsInvites',
    'ClanInvalidOperation',
    'ClanFounderCannotLeaveWithoutAbdication',
    'ClanNameReserved',
    'ClanApplicantInClanSoNowInvited',
    'ActivitiesUnknownException',
    'ActivitiesParameterNull',
    'ActivityCountsDiabled',
    'ActivitySearchInvalidParameters',
    'ActivityPermissionDenied',
    'ShareAlreadyShared',
    'ActivityLoggingDisabled',
    'ClanRequiresExistingDestinyAccount',
    'ClanNameRestricted',
    'ClanCreationBan',
    'ClanCreationTenureRequirementsNotMet',
    'ItemAlreadyFollowed',
    'ItemNotFollowed',
    'CannotFollowSelf',
    'GroupFollowLimitExceeded',
    'TagFollowLimitExceeded',
    'UserFollowLimitExceeded',
    'FollowUnsupportedEntityType',
    'NoValidTagsInList',
    'BelowMinimumSuggestionLength',
    'CannotGetSuggestionsOnMultipleTagsSimultaneously',
    'NotAValidPartialTag',
    'TagSuggestionsUnknownSqlResult',
    'TagsUnableToLoadPopularTagsFromDatabase',
    'TagInvalid',
    'TagNotFound',
    'SingleTagExpected',
    'TagsExceededMaximumPerItem',
    'IgnoreInvalidParameters',
    'IgnoreSqlException',
    'IgnoreErrorRetrievingGroupPermissions',
    'IgnoreErrorInsufficientPermission',
    'IgnoreErrorRetrievingItem',
    'IgnoreCannotIgnoreSelf',
    'IgnoreIllegalType',
    'IgnoreNotFound',
    'IgnoreUserGloballyIgnored',
    'IgnoreUserIgnored',
    'TargetUserIgnored',
    'NotificationSettingInvalid',
    'PsnApiExpiredAccessToken',
    'PSNExForbidden',
    'PSNExSystemDisabled',
    'PsnApiErrorCodeUnknown',
    'PsnApiErrorWebException',
    'PsnApiBadRequest',
    'PsnApiAccessTokenRequired',
    'PsnApiInvalidAccessToken',
    'PsnApiBannedUser',
    'PsnApiAccountUpgradeRequired',
    'PsnApiServiceTemporarilyUnavailable',
    'PsnApiServerBusy',
    'PsnApiUnderMaintenance',
    'PsnApiProfileUserNotFound',
    'PsnApiProfilePrivacyRestriction',
    'PsnApiProfileUnderMaintenance',
    'PsnApiAccountAttributeMissing',
    'PsnApiNoPermission',
    'PsnApiTargetUserBlocked',
    'PsnApiJwksMissing',
    'PsnApiJwtMalformedHeader',
    'PsnApiJwtMalformedPayload',
    'XblExSystemDisabled',
    'XblExUnknownError',
    'XblApiErrorWebException',
    'XblStsTokenInvalid',
    'XblStsMissingToken',
    'XblStsExpiredToken',
    'XblAccessToTheSandboxDenied',
    'XblMsaResponseMissing',
    'XblMsaAccessTokenExpired',
    'XblMsaInvalidRequest',
    'XblMsaFriendsRequireSignIn',
    'XblUserActionRequired',
    'XblParentalControls',
    'XblDeveloperAccount',
    'XblUserTokenExpired',
    'XblUserTokenInvalid',
    'XblOffline',
    'XblUnknownErrorCode',
    'XblMsaInvalidGrant',
    'ReportNotYetResolved',
    'ReportOverturnDoesNotChangeDecision',
    'ReportNotFound',
    'ReportAlreadyReported',
    'ReportInvalidResolution',
    'ReportNotAssignedToYou',
    'LegacyGameStatsSystemDisabled',
    'LegacyGameStatsUnknownError',
    'LegacyGameStatsMalformedSneakerNetCode',
    'DestinyAccountAcquisitionFailure',
    'DestinyAccountNotFound',
    'DestinyBuildStatsDatabaseError',
    'DestinyCharacterStatsDatabaseError',
    'DestinyPvPStatsDatabaseError',
    'DestinyPvEStatsDatabaseError',
    'DestinyGrimoireStatsDatabaseError',
    'DestinyStatsParameterMembershipTypeParseError',
    'DestinyStatsParameterMembershipIdParseError',
    'DestinyStatsParameterRangeParseError',
    'DestinyStringItemHashNotFound',
    'DestinyStringSetNotFound',
    'DestinyContentLookupNotFoundForKey',
    'DestinyContentItemNotFound',
    'DestinyContentSectionNotFound',
    'DestinyContentPropertyNotFound',
    'DestinyContentConfigNotFound',
    'DestinyContentPropertyBucketValueNotFound',
    'DestinyUnexpectedError',
    'DestinyInvalidAction',
    'DestinyCharacterNotFound',
    'DestinyInvalidFlag',
    'DestinyInvalidRequest',
    'DestinyItemNotFound',
    'DestinyInvalidCustomizationChoices',
    'DestinyVendorItemNotFound',
    'DestinyInternalError',
    'DestinyVendorNotFound',
    'DestinyRecentActivitiesDatabaseError',
    'DestinyItemBucketNotFound',
    'DestinyInvalidMembershipType',
    'DestinyVersionIncompatibility',
    'DestinyItemAlreadyInInventory',
    'DestinyBucketNotFound',
    'DestinyCharacterNotInTower',
    'DestinyCharacterNotLoggedIn',
    'DestinyDefinitionsNotLoaded',
    'DestinyInventoryFull',
    'DestinyItemFailedLevelCheck',
    'DestinyItemFailedUnlockCheck',
    'DestinyItemUnequippable',
    'DestinyItemUniqueEquipRestricted',
    'DestinyNoRoomInDestination',
    'DestinyServiceFailure',
    'DestinyServiceRetired',
    'DestinyTransferFailed',
    'DestinyTransferNotFoundForSourceBucket',
    'DestinyUnexpectedResultInVendorTransferCheck',
    'DestinyUniquenessViolation',
    'DestinyErrorDeserializationFailure',
    'DestinyValidAccountTicketRequired',
    'DestinyShardRelayClientTimeout',
    'DestinyShardRelayProxyTimeout',
    'DestinyPGCRNotFound',
    'DestinyAccountMustBeOffline',
    'DestinyCanOnlyEquipInGame',
    'DestinyCannotPerformActionOnEquippedItem',
    'DestinyQuestAlreadyCompleted',
    'DestinyQuestAlreadyTracked',
    'DestinyTrackableQuestsFull',
    'DestinyItemNotTransferrable',
    'DestinyVendorPurchaseNotAllowed',
    'DestinyContentVersionMismatch',
    'DestinyItemActionForbidden',
    'DestinyRefundInvalid',
    'DestinyPrivacyRestriction',
    'DestinyActionInsufficientPrivileges',
    'DestinyInvalidClaimException',
    'DestinyLegacyPlatformRestricted',
    'DestinyLegacyPlatformInUse',
    'DestinyLegacyPlatformInaccessible',
    'DestinyCannotPerformActionAtThisLocation',
    'DestinyThrottledByGameServer',
    'DestinyItemNotTransferrableHasSideEffects',
    'DestinyItemLocked',
    'DestinyCannotAffordMaterialRequirements',
    'DestinyFailedPlugInsertionRules',
    'DestinySocketNotFound',
    'DestinySocketActionNotAllowed',
    'DestinySocketAlreadyHasPlug',
    'DestinyPlugItemNotAvailable',
    'DestinyCharacterLoggedInNotAllowed',
    'DestinyPublicAccountNotAccessible',
    'DestinyClaimsItemAlreadyClaimed',
    'DestinyClaimsNoInventorySpace',
    'DestinyClaimsRequiredLevelNotMet',
    'DestinyClaimsInvalidState',
    'DestinyNotEnoughRoomForMultipleRewards',
    'DestinyDirectBabelClientTimeout',
    'FbInvalidRequest',
    'FbRedirectMismatch',
    'FbAccessDenied',
    'FbUnsupportedResponseType',
    'FbInvalidScope',
    'FbUnsupportedGrantType',
    'FbInvalidGrant',
    'InvitationExpired',
    'InvitationUnknownType',
    'InvitationInvalidResponseStatus',
    'InvitationInvalidType',
    'InvitationAlreadyPending',
    'InvitationInsufficientPermission',
    'InvitationInvalidCode',
    'InvitationInvalidTargetState',
    'InvitationCannotBeReactivated',
    'InvitationNoRecipients',
    'InvitationGroupCannotSendToSelf',
    'InvitationTooManyRecipients',
    'InvitationInvalid',
    'InvitationNotFound',
    'TokenInvalid',
    'TokenBadFormat',
    'TokenAlreadyClaimed',
    'TokenAlreadyClaimedSelf',
    'TokenThrottling',
    'TokenUnknownRedemptionFailure',
    'TokenPurchaseClaimFailedAfterTokenClaimed',
    'TokenUserAlreadyOwnsOffer',
    'TokenInvalidOfferKey',
    'TokenEmailNotValidated',
    'TokenProvisioningBadVendorOrOffer',
    'TokenPurchaseHistoryUnknownError',
    'TokenThrottleStateUnknownError',
    'TokenUserAgeNotVerified',
    'TokenExceededOfferMaximum',
    'TokenNoAvailableUnlocks',
    'TokenMarketplaceInvalidPlatform',
    'TokenNoMarketplaceCodesFound',
    'TokenOfferNotAvailableForRedemption',
    'TokenUnlockPartialFailure',
    'TokenMarketplaceInvalidRegion',
    'TokenOfferExpired',
    'RAFExceededMaximumReferrals',
    'RAFDuplicateBond',
    'RAFNoValidVeteranDestinyMembershipsFound',
    'RAFNotAValidVeteranUser',
    'RAFCodeAlreadyClaimedOrNotFound',
    'RAFMismatchedDestinyMembershipType',
    'RAFUnableToAccessPurchaseHistory',
    'RAFUnableToCreateBond',
    'RAFUnableToFindBond',
    'RAFUnableToRemoveBond',
    'RAFCannotBondToSelf',
    'RAFInvalidPlatform',
    'RAFGenerateThrottled',
    'RAFUnableToCreateBondVersionMismatch',
    'RAFUnableToRemoveBondVersionMismatch',
    'RAFRedeemThrottled',
    'NoAvailableDiscountCode',
    'DiscountAlreadyClaimed',
    'DiscountClaimFailure',
    'DiscountConfigurationFailure',
    'DiscountGenerationFailure',
    'DiscountAlreadyExists',
    'TokenRequiresCredentialXuid',
    'TokenRequiresCredentialPsnid',
    'OfferRequired',
    'UnknownEververseHistoryError',
    'MissingEververseHistoryError',
    'BungieRewardEmailStateInvalid',
    'BungieRewardNotYetClaimable',
    'MissingOfferConfig',
    'RAFQuestEntitlementRequiresBnet',
    'RAFQuestEntitlementTransportFailure',
    'RAFQuestEntitlementUnknownFailure',
    'RAFVeteranRewardUnknownFailure',
    'RAFTooEarlyToCancelBond',
    'LoyaltyRewardAlreadyRedeemed',
    'UnclaimedLoyaltyRewardEntryNotFound',
    'PartnerOfferPartialFailure',
    'PartnerOfferAlreadyClaimed',
    'PartnerOfferSkuNotFound',
    'PartnerOfferSkuExpired',
    'PartnerOfferPermissionFailure',
    'PartnerOfferNoDestinyAccount',
    'PartnerOfferApplyDataNotFound',
    'ApiExceededMaxKeys',
    'ApiInvalidOrExpiredKey',
    'ApiKeyMissingFromRequest',
    'ApplicationDisabled',
    'ApplicationExceededMax',
    'ApplicationDisallowedByScope',
    'AuthorizationCodeInvalid',
    'OriginHeaderDoesNotMatchKey',
    'AccessNotPermittedByApplicationScope',
    'ApplicationNameIsTaken',
    'RefreshTokenNotYetValid',
    'AccessTokenHasExpired',
    'ApplicationTokenFormatNotValid',
    'ApplicationNotConfiguredForBungieAuth',
    'ApplicationNotConfiguredForOAuth',
    'OAuthAccessTokenExpired',
    'ApplicationTokenKeyIdDoesNotExist',
    'ProvidedTokenNotValidRefreshToken',
    'RefreshTokenExpired',
    'AuthorizationRecordInvalid',
    'TokenPreviouslyRevoked',
    'TokenInvalidMembership',
    'AuthorizationCodeStale',
    'AuthorizationRecordExpired',
    'AuthorizationRecordRevoked',
    'AuthorizationRecordInactiveApiKey',
    'AuthorizationRecordApiKeyMatching',
    'PartnershipInvalidType',
    'PartnershipValidationError',
    'PartnershipValidationTimeout',
    'PartnershipAccessFailure',
    'PartnershipAccountInvalid',
    'PartnershipGetAccountInfoFailure',
    'PartnershipDisabled',
    'PartnershipAlreadyExists',
    'CommunityStreamingUnavailable',
    'TwitchNotLinked',
    'TwitchAccountNotFound',
    'TwitchCouldNotLoadDestinyInfo',
    'TwitchCouldNotRegisterUser',
    'TwitchCouldNotUnregisterUser',
    'TwitchRequiresRelinking',
    'TwitchNoPlatformChosen',
    'TrendingCategoryNotFound',
    'TrendingEntryTypeNotSupported',
    'ReportOffenderNotInPgcr',
    'ReportRequestorNotInPgcr',
    'ReportSubmissionFailed',
    'ReportCannotReportSelf',
    'AwaTypeDisabled',
    'AwaTooManyPendingRequests',
    'AwaTheFeatureRequiresARegisteredDevice',
    'AwaRequestWasUnansweredForTooLong',
    'AwaWriteRequestMissingOrInvalidToken',
    'AwaWriteRequestTokenExpired',
    'AwaWriteRequestTokenUsageLimitReached',
    'SteamWebApiError',
    'SteamWebNullResponseError',
    'SteamAccountRequired',
    'SteamNotAuthorized',
    'ClanFireteamNotFound',
    'ClanFireteamAddNoAlternatesForImmediate',
    'ClanFireteamFull',
    'ClanFireteamAltFull',
    'ClanFireteamBlocked',
    'ClanFireteamPlayerEntryNotFound',
    'ClanFireteamPermissions',
    'ClanFireteamInvalidPlatform',
    'ClanFireteamCannotAdjustSlotCount',
    'ClanFireteamInvalidPlayerPlatform',
    'ClanFireteamNotReadyForInvitesNotEnoughPlayers',
    'ClanFireteamGameInvitesNotSupportForPlatform',
    'ClanFireteamPlatformInvitePreqFailure',
    'ClanFireteamInvalidAuthContext',
    'ClanFireteamInvalidAuthProviderPsn',
    'ClanFireteamPs4SessionFull',
    'ClanFireteamInvalidAuthToken',
    'ClanFireteamScheduledFireteamsDisabled',
    'ClanFireteamNotReadyForInvitesNotScheduledYet',
    'ClanFireteamNotReadyForInvitesClosed',
    'ClanFireteamScheduledFireteamsRequireAdminPermissions',
    'ClanFireteamNonPublicMustHaveClan',
    'ClanFireteamPublicCreationRestriction',
    'ClanFireteamAlreadyJoined',
    'ClanFireteamScheduledFireteamsRange',
    'ClanFireteamPublicCreationRestrictionExtended',
    'ClanFireteamExpired',
    'ClanFireteamInvalidAuthProvider',
    'ClanFireteamInvalidAuthProviderXuid',
    'ClanFireteamThrottle',
    'ClanFireteamTooManyOpenScheduledFireteams',
    'ClanFireteamCannotReopenScheduledFireteams',
    'ClanFireteamJoinNoAccountSpecified',
    'ClanFireteamMinDestiny2ProgressForCreation',
    'ClanFireteamMinDestiny2ProgressForJoin',
    'ClanFireteamSMSOrPurchaseRequiredCreate',
    'ClanFireteamPurchaseRequiredCreate',
    'ClanFireteamSMSOrPurchaseRequiredJoin',
    'ClanFireteamPurchaseRequiredJoin',
    'CrossSaveOverriddenAccountNotFound',
    'CrossSaveTooManyOverriddenPlatforms',
    'CrossSaveNoOverriddenPlatforms',
    'CrossSavePrimaryAccountNotFound',
    'CrossSaveRequestInvalid',
    'CrossSaveBungieAccountValidationFailure',
    'CrossSaveOverriddenPlatformNotAllowed',
    'CrossSaveThresholdExceeded',
    'CrossSaveIncompatibleMembershipType',
    'CrossSaveCouldNotFindLinkedAccountForMembershipType',
    'CrossSaveCouldNotCreateDestinyProfileForMembershipType',
    'CrossSaveErrorCreatingDestinyProfileForMembershipType',
    'CrossSaveCannotOverrideSelf',
    'CrossSaveRecentSilverPurchase',
    'CrossSaveSilverBalanceNegative',
    'CrossSaveAccountNotAuthenticated',
    'ErrorOneAccountAlreadyActive',
    'ErrorOneAccountDestinyRestriction',
    'CrossSaveMustMigrateToSteam',
    'CrossSaveSteamAlreadyPaired',
    'CrossSaveCannotPairJustSteamAndBlizzard',
    'CrossSaveCannotPairSteamAloneBeforeShadowkeep',
    'AuthVerificationNotLinkedToAccount',
    'PCMigrationMissingBlizzard',
    'PCMigrationMissingSteam',
    'PCMigrationInvalidBlizzard',
    'PCMigrationInvalidSteam',
    'PCMigrationUnknownFailure',
    'PCMigrationUnknownException',
    'PCMigrationNotLinked',
    'PCMigrationAccountsAlreadyUsed',
    'PCMigrationStepFailed',
    'PCMigrationInvalidBlizzardCrossSaveState',
    'PCMigrationDestinationBanned',
    'PCMigrationDestinyFailure',
    'PCMigrationSilverTransferFailed',
    'PCMigrationEntitlementTransferFailed',
    'PCMigrationCannotStompClanFounder',
    'UnsupportedBrowser',
    'StadiaAccountRequired',
    'ErrorPhoneValidationTooManyUses',
    'ErrorPhoneValidationNoAssociatedPhone',
    'ErrorPhoneValidationCodeInvalid',
    'ErrorPhoneValidationBanned',
    'ErrorPhoneValidationCodeTooRecentlySent',
    'ErrorPhoneValidationCodeExpired',
    'ErrorPhoneValidationInvalidNumberType',
    'ErrorPhoneValidationCodeTooRecentlyChecked',
    'ApplePushErrorUnknown',
    'ApplePushErrorNull',
    'ApplePushErrorTimeout',
    'ApplePushBadRequest',
    'ApplePushFailedAuth',
    'ApplePushThrottled',
    'ApplePushServiceUnavailable',
    'NotAnImageOrVideo',
    'ErrorBungieFriendsBlockFailed',
    'ErrorBungieFriendsAutoReject',
    'ErrorBungieFriendsNoRequestFound',
    'ErrorBungieFriendsAlreadyFriends',
    'ErrorBungieFriendsUnableToRemoveRequest',
    'ErrorBungieFriendsUnableToRemove',
    'ErrorBungieFriendsIdenticalSourceTarget',
    'ErrorBungieFriendsSelf',
    'ErrorBungieBlockSelf',
    'ErrorBungieFriendsListFull',
    'ErrorBungieBlockListFull',
]


class DestinyException(Exception):
    pass


class ObsoleteError(DestinyException):
    pass


class ApiInvalidOrExpiredKey(DestinyException):
    pass


class None_(DestinyException):
    pass


class Success(DestinyException):
    pass


class TransportException(DestinyException):
    pass


class UnhandledException(DestinyException):
    pass


class NotImplemented(DestinyException):
    pass


class SystemDisabled(DestinyException):
    pass


class FailedToLoadAvailableLocalesConfiguration(DestinyException):
    pass


class ParameterParseFailure(DestinyException):
    pass


class ParameterInvalidRange(DestinyException):
    pass


class BadRequest(DestinyException):
    pass


class AuthenticationInvalid(DestinyException):
    pass


class DataNotFound(DestinyException):
    pass


class InsufficientPrivileges(DestinyException):
    pass


class Duplicate(DestinyException):
    pass


class UnknownSqlResult(DestinyException):
    pass


class ValidationError(DestinyException):
    pass


class ValidationMissingFieldError(DestinyException):
    pass


class ValidationInvalidInputError(DestinyException):
    pass


class InvalidParameters(DestinyException):
    pass


class ParameterNotFound(DestinyException):
    pass


class UnhandledHttpException(DestinyException):
    pass


class NotFound(DestinyException):
    pass


class WebAuthModuleAsyncFailed(DestinyException):
    pass


class InvalidReturnValue(DestinyException):
    pass


class UserBanned(DestinyException):
    pass


class InvalidPostBody(DestinyException):
    pass


class MissingPostBody(DestinyException):
    pass


class ExternalServiceTimeout(DestinyException):
    pass


class ValidationLengthError(DestinyException):
    pass


class ValidationRangeError(DestinyException):
    pass


class JsonDeserializationError(DestinyException):
    pass


class ThrottleLimitExceeded(DestinyException):
    pass


class ValidationTagError(DestinyException):
    pass


class ValidationProfanityError(DestinyException):
    pass


class ValidationUrlFormatError(DestinyException):
    pass


class ThrottleLimitExceededMinutes(DestinyException):
    pass


class ThrottleLimitExceededMomentarily(DestinyException):
    pass


class ThrottleLimitExceededSeconds(DestinyException):
    pass


class ExternalServiceUnknown(DestinyException):
    pass


class ValidationWordLengthError(DestinyException):
    pass


class ValidationInvisibleUnicode(DestinyException):
    pass


class ValidationBadNames(DestinyException):
    pass


class ExternalServiceFailed(DestinyException):
    pass


class ServiceRetired(DestinyException):
    pass


class UnknownSqlException(DestinyException):
    pass


class UnsupportedLocale(DestinyException):
    pass


class InvalidPageNumber(DestinyException):
    pass


class MaximumPageSizeExceeded(DestinyException):
    pass


class ServiceUnsupported(DestinyException):
    pass


class ValidationMaximumUnicodeCombiningCharacters(DestinyException):
    pass


class ValidationMaximumSequentialCarriageReturns(DestinyException):
    pass


class PerEndpointRequestThrottleExceeded(DestinyException):
    pass


class AuthContextCacheAssertion(DestinyException):
    pass


class ExPlatformStringValidationError(DestinyException):
    pass


class PerApplicationThrottleExceeded(DestinyException):
    pass


class PerApplicationAnonymousThrottleExceeded(DestinyException):
    pass


class PerApplicationAuthenticatedThrottleExceeded(DestinyException):
    pass


class PerUserThrottleExceeded(DestinyException):
    pass


class PayloadSignatureVerificationFailure(DestinyException):
    pass


class InvalidServiceAuthContext(DestinyException):
    pass


class ObsoleteCredentialType(DestinyException):
    pass


class UnableToUnPairMobileApp(DestinyException):
    pass


class UnableToPairMobileApp(DestinyException):
    pass


class CannotUseMobileAuthWithNonMobileProvider(DestinyException):
    pass


class MissingDeviceCookie(DestinyException):
    pass


class FacebookTokenExpired(DestinyException):
    pass


class AuthTicketRequired(DestinyException):
    pass


class CookieContextRequired(DestinyException):
    pass


class UnknownAuthenticationError(DestinyException):
    pass


class BungieNetAccountCreationRequired(DestinyException):
    pass


class WebAuthRequired(DestinyException):
    pass


class ContentUnknownSqlResult(DestinyException):
    pass


class ContentNeedUniquePath(DestinyException):
    pass


class ContentSqlException(DestinyException):
    pass


class ContentNotFound(DestinyException):
    pass


class ContentSuccessWithTagAddFail(DestinyException):
    pass


class ContentSearchMissingParameters(DestinyException):
    pass


class ContentInvalidId(DestinyException):
    pass


class ContentPhysicalFileDeletionError(DestinyException):
    pass


class ContentPhysicalFileCreationError(DestinyException):
    pass


class ContentPerforceSubmissionError(DestinyException):
    pass


class ContentPerforceInitializationError(DestinyException):
    pass


class ContentDeploymentPackageNotReadyError(DestinyException):
    pass


class ContentUploadFailed(DestinyException):
    pass


class ContentTooManyResults(DestinyException):
    pass


class ContentInvalidState(DestinyException):
    pass


class ContentNavigationParentNotFound(DestinyException):
    pass


class ContentNavigationParentUpdateError(DestinyException):
    pass


class DeploymentPackageNotEditable(DestinyException):
    pass


class ContentValidationError(DestinyException):
    pass


class ContentPropertiesValidationError(DestinyException):
    pass


class ContentTypeNotFound(DestinyException):
    pass


class DeploymentPackageNotFound(DestinyException):
    pass


class ContentSearchInvalidParameters(DestinyException):
    pass


class ContentItemPropertyAggregationError(DestinyException):
    pass


class DeploymentPackageFileNotFound(DestinyException):
    pass


class ContentPerforceFileHistoryNotFound(DestinyException):
    pass


class ContentAssetZipCreationFailure(DestinyException):
    pass


class ContentAssetZipCreationBusy(DestinyException):
    pass


class ContentProjectNotFound(DestinyException):
    pass


class ContentFolderNotFound(DestinyException):
    pass


class ContentPackagesInconsistent(DestinyException):
    pass


class ContentPackagesInvalidState(DestinyException):
    pass


class ContentPackagesInconsistentType(DestinyException):
    pass


class ContentCannotDeletePackage(DestinyException):
    pass


class ContentLockedForChanges(DestinyException):
    pass


class ContentFileUploadFailed(DestinyException):
    pass


class ContentNotReviewed(DestinyException):
    pass


class ContentPermissionDenied(DestinyException):
    pass


class ContentInvalidExternalUrl(DestinyException):
    pass


class ContentExternalFileCannotBeImportedLocally(DestinyException):
    pass


class ContentTagSaveFailure(DestinyException):
    pass


class ContentPerforceUnmatchedFileError(DestinyException):
    pass


class ContentPerforceChangelistResultNotFound(DestinyException):
    pass


class ContentPerforceChangelistFileItemsNotFound(DestinyException):
    pass


class ContentPerforceInvalidRevisionError(DestinyException):
    pass


class ContentUnloadedSaveResult(DestinyException):
    pass


class ContentPropertyInvalidNumber(DestinyException):
    pass


class ContentPropertyInvalidUrl(DestinyException):
    pass


class ContentPropertyInvalidDate(DestinyException):
    pass


class ContentPropertyInvalidSet(DestinyException):
    pass


class ContentPropertyCannotDeserialize(DestinyException):
    pass


class ContentRegexValidationFailOnProperty(DestinyException):
    pass


class ContentMaxLengthFailOnProperty(DestinyException):
    pass


class ContentPropertyUnexpectedDeserializationError(DestinyException):
    pass


class ContentPropertyRequired(DestinyException):
    pass


class ContentCannotCreateFile(DestinyException):
    pass


class ContentInvalidMigrationFile(DestinyException):
    pass


class ContentMigrationAlteringProcessedItem(DestinyException):
    pass


class ContentPropertyDefinitionNotFound(DestinyException):
    pass


class ContentReviewDataChanged(DestinyException):
    pass


class ContentRollbackRevisionNotInPackage(DestinyException):
    pass


class ContentItemNotBasedOnLatestRevision(DestinyException):
    pass


class ContentUnauthorized(DestinyException):
    pass


class ContentCannotCreateDeploymentPackage(DestinyException):
    pass


class ContentUserNotFound(DestinyException):
    pass


class ContentLocalePermissionDenied(DestinyException):
    pass


class ContentInvalidLinkToInternalEnvironment(DestinyException):
    pass


class ContentInvalidBlacklistedContent(DestinyException):
    pass


class ContentMacroMalformedNoContentId(DestinyException):
    pass


class ContentMacroMalformedNoTemplateType(DestinyException):
    pass


class ContentIllegalBNetMembershipId(DestinyException):
    pass


class ContentLocaleDidNotMatchExpected(DestinyException):
    pass


class ContentBabelCallFailed(DestinyException):
    pass


class ContentEnglishPostLiveForbidden(DestinyException):
    pass


class ContentLocaleEditPermissionDenied(DestinyException):
    pass


class UserNonUniqueName(DestinyException):
    pass


class UserManualLinkingStepRequired(DestinyException):
    pass


class UserCreateUnknownSqlResult(DestinyException):
    pass


class UserCreateUnknownSqlException(DestinyException):
    pass


class UserMalformedMembershipId(DestinyException):
    pass


class UserCannotFindRequestedUser(DestinyException):
    pass


class UserCannotLoadAccountCredentialLinkInfo(DestinyException):
    pass


class UserInvalidMobileAppType(DestinyException):
    pass


class UserMissingMobilePairingInfo(DestinyException):
    pass


class UserCannotGenerateMobileKeyWhileUsingMobileCredential(DestinyException):
    pass


class UserGenerateMobileKeyExistingSlotCollision(DestinyException):
    pass


class UserDisplayNameMissingOrInvalid(DestinyException):
    pass


class UserCannotLoadAccountProfileData(DestinyException):
    pass


class UserCannotSaveUserProfileData(DestinyException):
    pass


class UserEmailMissingOrInvalid(DestinyException):
    pass


class UserTermsOfUseRequired(DestinyException):
    pass


class UserCannotCreateNewAccountWhileLoggedIn(DestinyException):
    pass


class UserCannotResolveCentralAccount(DestinyException):
    pass


class UserInvalidAvatar(DestinyException):
    pass


class UserMissingCreatedUserResult(DestinyException):
    pass


class UserCannotChangeUniqueNameYet(DestinyException):
    pass


class UserCannotChangeDisplayNameYet(DestinyException):
    pass


class UserCannotChangeEmail(DestinyException):
    pass


class UserUniqueNameMustStartWithLetter(DestinyException):
    pass


class UserNoLinkedAccountsSupportFriendListings(DestinyException):
    pass


class UserAcknowledgmentTableFull(DestinyException):
    pass


class UserCreationDestinyMembershipRequired(DestinyException):
    pass


class UserFriendsTokenNeedsRefresh(DestinyException):
    pass


class UserEmailValidationUnknown(DestinyException):
    pass


class UserEmailValidationLimit(DestinyException):
    pass


class TransactionEmailSendFailure(DestinyException):
    pass


class MailHookPermissionFailure(DestinyException):
    pass


class MailServiceRateLimit(DestinyException):
    pass


class UserEmailMustBeVerified(DestinyException):
    pass


class UserMustAllowCustomerServiceEmails(DestinyException):
    pass


class NonTransactionalEmailSendFailure(DestinyException):
    pass


class UnknownErrorSettingGlobalDisplayName(DestinyException):
    pass


class DuplicateGlobalDisplayName(DestinyException):
    pass


class ErrorRunningNameValidationChecks(DestinyException):
    pass


class ErrorDatabaseGlobalName(DestinyException):
    pass


class ErrorNoAvailableNameChanges(DestinyException):
    pass


class ErrorNameAlreadySetToInput(DestinyException):
    pass


class MessagingUnknownError(DestinyException):
    pass


class MessagingSelfError(DestinyException):
    pass


class MessagingSendThrottle(DestinyException):
    pass


class MessagingNoBody(DestinyException):
    pass


class MessagingTooManyUsers(DestinyException):
    pass


class MessagingCanNotLeaveConversation(DestinyException):
    pass


class MessagingUnableToSend(DestinyException):
    pass


class MessagingDeletedUserForbidden(DestinyException):
    pass


class MessagingCannotDeleteExternalConversation(DestinyException):
    pass


class MessagingGroupChatDisabled(DestinyException):
    pass


class MessagingMustIncludeSelfInPrivateMessage(DestinyException):
    pass


class MessagingSenderIsBanned(DestinyException):
    pass


class MessagingGroupOptionalChatExceededMaximum(DestinyException):
    pass


class PrivateMessagingRequiresDestinyMembership(DestinyException):
    pass


class AddSurveyAnswersUnknownSqlException(DestinyException):
    pass


class ForumBodyCannotBeEmpty(DestinyException):
    pass


class ForumSubjectCannotBeEmptyOnTopicPost(DestinyException):
    pass


class ForumCannotLocateParentPost(DestinyException):
    pass


class ForumThreadLockedForReplies(DestinyException):
    pass


class ForumUnknownSqlResultDuringCreatePost(DestinyException):
    pass


class ForumUnknownTagCreationError(DestinyException):
    pass


class ForumUnknownSqlResultDuringTagItem(DestinyException):
    pass


class ForumUnknownExceptionCreatePost(DestinyException):
    pass


class ForumQuestionMustBeTopicPost(DestinyException):
    pass


class ForumExceptionDuringTagSearch(DestinyException):
    pass


class ForumExceptionDuringTopicRetrieval(DestinyException):
    pass


class ForumAliasedTagError(DestinyException):
    pass


class ForumCannotLocateThread(DestinyException):
    pass


class ForumUnknownExceptionEditPost(DestinyException):
    pass


class ForumCannotLocatePost(DestinyException):
    pass


class ForumUnknownExceptionGetOrCreateTags(DestinyException):
    pass


class ForumEditPermissionDenied(DestinyException):
    pass


class ForumUnknownSqlResultDuringTagIdRetrieval(DestinyException):
    pass


class ForumCannotGetRating(DestinyException):
    pass


class ForumUnknownExceptionGetRating(DestinyException):
    pass


class ForumRatingsAccessError(DestinyException):
    pass


class ForumRelatedPostAccessError(DestinyException):
    pass


class ForumLatestReplyAccessError(DestinyException):
    pass


class ForumUserStatusAccessError(DestinyException):
    pass


class ForumAuthorAccessError(DestinyException):
    pass


class ForumGroupAccessError(DestinyException):
    pass


class ForumUrlExpectedButMissing(DestinyException):
    pass


class ForumRepliesCannotBeEmpty(DestinyException):
    pass


class ForumRepliesCannotBeInDifferentGroups(DestinyException):
    pass


class ForumSubTopicCannotBeCreatedAtThisThreadLevel(DestinyException):
    pass


class ForumCannotCreateContentTopic(DestinyException):
    pass


class ForumTopicDoesNotExist(DestinyException):
    pass


class ForumContentCommentsNotAllowed(DestinyException):
    pass


class ForumUnknownSqlResultDuringEditPost(DestinyException):
    pass


class ForumUnknownSqlResultDuringGetPost(DestinyException):
    pass


class ForumPostValidationBadUrl(DestinyException):
    pass


class ForumBodyTooLong(DestinyException):
    pass


class ForumSubjectTooLong(DestinyException):
    pass


class ForumAnnouncementNotAllowed(DestinyException):
    pass


class ForumCannotShareOwnPost(DestinyException):
    pass


class ForumEditNoOp(DestinyException):
    pass


class ForumUnknownDatabaseErrorDuringGetPost(DestinyException):
    pass


class ForumExceeedMaximumRowLimit(DestinyException):
    pass


class ForumCannotSharePrivatePost(DestinyException):
    pass


class ForumCannotCrossPostBetweenGroups(DestinyException):
    pass


class ForumIncompatibleCategories(DestinyException):
    pass


class ForumCannotUseTheseCategoriesOnNonTopicPost(DestinyException):
    pass


class ForumCanOnlyDeleteTopics(DestinyException):
    pass


class ForumDeleteSqlException(DestinyException):
    pass


class ForumDeleteSqlUnknownResult(DestinyException):
    pass


class ForumTooManyTags(DestinyException):
    pass


class ForumCanOnlyRateTopics(DestinyException):
    pass


class ForumBannedPostsCannotBeEdited(DestinyException):
    pass


class ForumThreadRootIsBanned(DestinyException):
    pass


class ForumCannotUseOfficialTagCategoryAsTag(DestinyException):
    pass


class ForumAnswerCannotBeMadeOnCreatePost(DestinyException):
    pass


class ForumAnswerCannotBeMadeOnEditPost(DestinyException):
    pass


class ForumAnswerPostIdIsNotADirectReplyOfQuestion(DestinyException):
    pass


class ForumAnswerTopicIdIsNotAQuestion(DestinyException):
    pass


class ForumUnknownExceptionDuringMarkAnswer(DestinyException):
    pass


class ForumUnknownSqlResultDuringMarkAnswer(DestinyException):
    pass


class ForumCannotRateYourOwnPosts(DestinyException):
    pass


class ForumPollsMustBeTheFirstPostInTopic(DestinyException):
    pass


class ForumInvalidPollInput(DestinyException):
    pass


class ForumGroupAdminEditNonMember(DestinyException):
    pass


class ForumCannotEditModeratorEditedPost(DestinyException):
    pass


class ForumRequiresDestinyMembership(DestinyException):
    pass


class ForumUnexpectedError(DestinyException):
    pass


class ForumAgeLock(DestinyException):
    pass


class ForumMaxPages(DestinyException):
    pass


class ForumMaxPagesOldestFirst(DestinyException):
    pass


class ForumCannotApplyForumIdWithoutTags(DestinyException):
    pass


class ForumCannotApplyForumIdToNonTopics(DestinyException):
    pass


class ForumCannotDownvoteCommunityCreations(DestinyException):
    pass


class ForumTopicsMustHaveOfficialCategory(DestinyException):
    pass


class ForumRecruitmentTopicMalformed(DestinyException):
    pass


class ForumRecruitmentTopicNotFound(DestinyException):
    pass


class ForumRecruitmentTopicNoSlotsRemaining(DestinyException):
    pass


class ForumRecruitmentTopicKickBan(DestinyException):
    pass


class ForumRecruitmentTopicRequirementsNotMet(DestinyException):
    pass


class ForumRecruitmentTopicNoPlayers(DestinyException):
    pass


class ForumRecruitmentApproveFailMessageBan(DestinyException):
    pass


class ForumRecruitmentGlobalBan(DestinyException):
    pass


class ForumUserBannedFromThisTopic(DestinyException):
    pass


class ForumRecruitmentFireteamMembersOnly(DestinyException):
    pass


class ForumRequiresDestiny2Progress(DestinyException):
    pass


class GroupMembershipApplicationAlreadyResolved(DestinyException):
    pass


class GroupMembershipAlreadyApplied(DestinyException):
    pass


class GroupMembershipInsufficientPrivileges(DestinyException):
    pass


class GroupIdNotReturnedFromCreation(DestinyException):
    pass


class GroupSearchInvalidParameters(DestinyException):
    pass


class GroupMembershipPendingApplicationNotFound(DestinyException):
    pass


class GroupInvalidId(DestinyException):
    pass


class GroupInvalidMembershipId(DestinyException):
    pass


class GroupInvalidMembershipType(DestinyException):
    pass


class GroupMissingTags(DestinyException):
    pass


class GroupMembershipNotFound(DestinyException):
    pass


class GroupInvalidRating(DestinyException):
    pass


class GroupUserFollowingAccessError(DestinyException):
    pass


class GroupUserMembershipAccessError(DestinyException):
    pass


class GroupCreatorAccessError(DestinyException):
    pass


class GroupAdminAccessError(DestinyException):
    pass


class GroupPrivatePostNotViewable(DestinyException):
    pass


class GroupMembershipNotLoggedIn(DestinyException):
    pass


class GroupNotDeleted(DestinyException):
    pass


class GroupUnknownErrorUndeletingGroup(DestinyException):
    pass


class GroupDeleted(DestinyException):
    pass


class GroupNotFound(DestinyException):
    pass


class GroupMemberBanned(DestinyException):
    pass


class GroupMembershipClosed(DestinyException):
    pass


class GroupPrivatePostOverrideError(DestinyException):
    pass


class GroupNameTaken(DestinyException):
    pass


class GroupDeletionGracePeriodExpired(DestinyException):
    pass


class GroupCannotCheckBanStatus(DestinyException):
    pass


class GroupMaximumMembershipCountReached(DestinyException):
    pass


class NoDestinyAccountForClanPlatform(DestinyException):
    pass


class AlreadyRequestingMembershipForClanPlatform(DestinyException):
    pass


class AlreadyClanMemberOnPlatform(DestinyException):
    pass


class GroupJoinedCannotSetClanName(DestinyException):
    pass


class GroupLeftCannotClearClanName(DestinyException):
    pass


class GroupRelationshipRequestPending(DestinyException):
    pass


class GroupRelationshipRequestBlocked(DestinyException):
    pass


class GroupRelationshipRequestNotFound(DestinyException):
    pass


class GroupRelationshipBlockNotFound(DestinyException):
    pass


class GroupRelationshipNotFound(DestinyException):
    pass


class GroupAlreadyAllied(DestinyException):
    pass


class GroupAlreadyMember(DestinyException):
    pass


class GroupRelationshipAlreadyExists(DestinyException):
    pass


class InvalidGroupTypesForRelationshipRequest(DestinyException):
    pass


class GroupAtMaximumAlliances(DestinyException):
    pass


class GroupCannotSetClanOnlySettings(DestinyException):
    pass


class ClanCannotSetTwoDefaultPostTypes(DestinyException):
    pass


class GroupMemberInvalidMemberType(DestinyException):
    pass


class GroupInvalidPlatformType(DestinyException):
    pass


class GroupMemberInvalidSort(DestinyException):
    pass


class GroupInvalidResolveState(DestinyException):
    pass


class ClanAlreadyEnabledForPlatform(DestinyException):
    pass


class ClanNotEnabledForPlatform(DestinyException):
    pass


class ClanEnabledButCouldNotJoinNoAccount(DestinyException):
    pass


class ClanEnabledButCouldNotJoinAlreadyMember(DestinyException):
    pass


class ClanCannotJoinNoCredential(DestinyException):
    pass


class NoClanMembershipForPlatform(DestinyException):
    pass


class GroupToGroupFollowLimitReached(DestinyException):
    pass


class ChildGroupAlreadyInAlliance(DestinyException):
    pass


class OwnerGroupAlreadyInAlliance(DestinyException):
    pass


class AllianceOwnerCannotJoinAlliance(DestinyException):
    pass


class GroupNotInAlliance(DestinyException):
    pass


class ChildGroupCannotInviteToAlliance(DestinyException):
    pass


class GroupToGroupAlreadyFollowed(DestinyException):
    pass


class GroupToGroupNotFollowing(DestinyException):
    pass


class ClanMaximumMembershipReached(DestinyException):
    pass


class ClanNameNotValid(DestinyException):
    pass


class ClanNameNotValidError(DestinyException):
    pass


class AllianceOwnerNotDefined(DestinyException):
    pass


class AllianceChildNotDefined(DestinyException):
    pass


class ClanCultureIllegalCharacters(DestinyException):
    pass


class ClanTagIllegalCharacters(DestinyException):
    pass


class ClanRequiresInvitation(DestinyException):
    pass


class ClanMembershipClosed(DestinyException):
    pass


class ClanInviteAlreadyMember(DestinyException):
    pass


class GroupInviteAlreadyMember(DestinyException):
    pass


class GroupJoinApprovalRequired(DestinyException):
    pass


class ClanTagRequired(DestinyException):
    pass


class GroupNameCannotStartOrEndWithWhiteSpace(DestinyException):
    pass


class ClanCallsignCannotStartOrEndWithWhiteSpace(DestinyException):
    pass


class ClanMigrationFailed(DestinyException):
    pass


class ClanNotEnabledAlreadyMemberOfAnotherClan(DestinyException):
    pass


class GroupModerationNotPermittedOnNonMembers(DestinyException):
    pass


class ClanCreationInWorldServerFailed(DestinyException):
    pass


class ClanNotFound(DestinyException):
    pass


class ClanMembershipLevelDoesNotPermitThatAction(DestinyException):
    pass


class ClanMemberNotFound(DestinyException):
    pass


class ClanMissingMembershipApprovers(DestinyException):
    pass


class ClanInWrongStateForRequestedAction(DestinyException):
    pass


class ClanNameAlreadyUsed(DestinyException):
    pass


class ClanTooFewMembers(DestinyException):
    pass


class ClanInfoCannotBeWhitespace(DestinyException):
    pass


class GroupCultureThrottle(DestinyException):
    pass


class ClanTargetDisallowsInvites(DestinyException):
    pass


class ClanInvalidOperation(DestinyException):
    pass


class ClanFounderCannotLeaveWithoutAbdication(DestinyException):
    pass


class ClanNameReserved(DestinyException):
    pass


class ClanApplicantInClanSoNowInvited(DestinyException):
    pass


class ActivitiesUnknownException(DestinyException):
    pass


class ActivitiesParameterNull(DestinyException):
    pass


class ActivityCountsDiabled(DestinyException):
    pass


class ActivitySearchInvalidParameters(DestinyException):
    pass


class ActivityPermissionDenied(DestinyException):
    pass


class ShareAlreadyShared(DestinyException):
    pass


class ActivityLoggingDisabled(DestinyException):
    pass


class ClanRequiresExistingDestinyAccount(DestinyException):
    pass


class ClanNameRestricted(DestinyException):
    pass


class ClanCreationBan(DestinyException):
    pass


class ClanCreationTenureRequirementsNotMet(DestinyException):
    pass


class ItemAlreadyFollowed(DestinyException):
    pass


class ItemNotFollowed(DestinyException):
    pass


class CannotFollowSelf(DestinyException):
    pass


class GroupFollowLimitExceeded(DestinyException):
    pass


class TagFollowLimitExceeded(DestinyException):
    pass


class UserFollowLimitExceeded(DestinyException):
    pass


class FollowUnsupportedEntityType(DestinyException):
    pass


class NoValidTagsInList(DestinyException):
    pass


class BelowMinimumSuggestionLength(DestinyException):
    pass


class CannotGetSuggestionsOnMultipleTagsSimultaneously(DestinyException):
    pass


class NotAValidPartialTag(DestinyException):
    pass


class TagSuggestionsUnknownSqlResult(DestinyException):
    pass


class TagsUnableToLoadPopularTagsFromDatabase(DestinyException):
    pass


class TagInvalid(DestinyException):
    pass


class TagNotFound(DestinyException):
    pass


class SingleTagExpected(DestinyException):
    pass


class TagsExceededMaximumPerItem(DestinyException):
    pass


class IgnoreInvalidParameters(DestinyException):
    pass


class IgnoreSqlException(DestinyException):
    pass


class IgnoreErrorRetrievingGroupPermissions(DestinyException):
    pass


class IgnoreErrorInsufficientPermission(DestinyException):
    pass


class IgnoreErrorRetrievingItem(DestinyException):
    pass


class IgnoreCannotIgnoreSelf(DestinyException):
    pass


class IgnoreIllegalType(DestinyException):
    pass


class IgnoreNotFound(DestinyException):
    pass


class IgnoreUserGloballyIgnored(DestinyException):
    pass


class IgnoreUserIgnored(DestinyException):
    pass


class TargetUserIgnored(DestinyException):
    pass


class NotificationSettingInvalid(DestinyException):
    pass


class PsnApiExpiredAccessToken(DestinyException):
    pass


class PSNExForbidden(DestinyException):
    pass


class PSNExSystemDisabled(DestinyException):
    pass


class PsnApiErrorCodeUnknown(DestinyException):
    pass


class PsnApiErrorWebException(DestinyException):
    pass


class PsnApiBadRequest(DestinyException):
    pass


class PsnApiAccessTokenRequired(DestinyException):
    pass


class PsnApiInvalidAccessToken(DestinyException):
    pass


class PsnApiBannedUser(DestinyException):
    pass


class PsnApiAccountUpgradeRequired(DestinyException):
    pass


class PsnApiServiceTemporarilyUnavailable(DestinyException):
    pass


class PsnApiServerBusy(DestinyException):
    pass


class PsnApiUnderMaintenance(DestinyException):
    pass


class PsnApiProfileUserNotFound(DestinyException):
    pass


class PsnApiProfilePrivacyRestriction(DestinyException):
    pass


class PsnApiProfileUnderMaintenance(DestinyException):
    pass


class PsnApiAccountAttributeMissing(DestinyException):
    pass


class PsnApiNoPermission(DestinyException):
    pass


class PsnApiTargetUserBlocked(DestinyException):
    pass


class PsnApiJwksMissing(DestinyException):
    pass


class PsnApiJwtMalformedHeader(DestinyException):
    pass


class PsnApiJwtMalformedPayload(DestinyException):
    pass


class XblExSystemDisabled(DestinyException):
    pass


class XblExUnknownError(DestinyException):
    pass


class XblApiErrorWebException(DestinyException):
    pass


class XblStsTokenInvalid(DestinyException):
    pass


class XblStsMissingToken(DestinyException):
    pass


class XblStsExpiredToken(DestinyException):
    pass


class XblAccessToTheSandboxDenied(DestinyException):
    pass


class XblMsaResponseMissing(DestinyException):
    pass


class XblMsaAccessTokenExpired(DestinyException):
    pass


class XblMsaInvalidRequest(DestinyException):
    pass


class XblMsaFriendsRequireSignIn(DestinyException):
    pass


class XblUserActionRequired(DestinyException):
    pass


class XblParentalControls(DestinyException):
    pass


class XblDeveloperAccount(DestinyException):
    pass


class XblUserTokenExpired(DestinyException):
    pass


class XblUserTokenInvalid(DestinyException):
    pass


class XblOffline(DestinyException):
    pass


class XblUnknownErrorCode(DestinyException):
    pass


class XblMsaInvalidGrant(DestinyException):
    pass


class ReportNotYetResolved(DestinyException):
    pass


class ReportOverturnDoesNotChangeDecision(DestinyException):
    pass


class ReportNotFound(DestinyException):
    pass


class ReportAlreadyReported(DestinyException):
    pass


class ReportInvalidResolution(DestinyException):
    pass


class ReportNotAssignedToYou(DestinyException):
    pass


class LegacyGameStatsSystemDisabled(DestinyException):
    pass


class LegacyGameStatsUnknownError(DestinyException):
    pass


class LegacyGameStatsMalformedSneakerNetCode(DestinyException):
    pass


class DestinyAccountAcquisitionFailure(DestinyException):
    pass


class DestinyAccountNotFound(DestinyException):
    pass


class DestinyBuildStatsDatabaseError(DestinyException):
    pass


class DestinyCharacterStatsDatabaseError(DestinyException):
    pass


class DestinyPvPStatsDatabaseError(DestinyException):
    pass


class DestinyPvEStatsDatabaseError(DestinyException):
    pass


class DestinyGrimoireStatsDatabaseError(DestinyException):
    pass


class DestinyStatsParameterMembershipTypeParseError(DestinyException):
    pass


class DestinyStatsParameterMembershipIdParseError(DestinyException):
    pass


class DestinyStatsParameterRangeParseError(DestinyException):
    pass


class DestinyStringItemHashNotFound(DestinyException):
    pass


class DestinyStringSetNotFound(DestinyException):
    pass


class DestinyContentLookupNotFoundForKey(DestinyException):
    pass


class DestinyContentItemNotFound(DestinyException):
    pass


class DestinyContentSectionNotFound(DestinyException):
    pass


class DestinyContentPropertyNotFound(DestinyException):
    pass


class DestinyContentConfigNotFound(DestinyException):
    pass


class DestinyContentPropertyBucketValueNotFound(DestinyException):
    pass


class DestinyUnexpectedError(DestinyException):
    pass


class DestinyInvalidAction(DestinyException):
    pass


class DestinyCharacterNotFound(DestinyException):
    pass


class DestinyInvalidFlag(DestinyException):
    pass


class DestinyInvalidRequest(DestinyException):
    pass


class DestinyItemNotFound(DestinyException):
    pass


class DestinyInvalidCustomizationChoices(DestinyException):
    pass


class DestinyVendorItemNotFound(DestinyException):
    pass


class DestinyInternalError(DestinyException):
    pass


class DestinyVendorNotFound(DestinyException):
    pass


class DestinyRecentActivitiesDatabaseError(DestinyException):
    pass


class DestinyItemBucketNotFound(DestinyException):
    pass


class DestinyInvalidMembershipType(DestinyException):
    pass


class DestinyVersionIncompatibility(DestinyException):
    pass


class DestinyItemAlreadyInInventory(DestinyException):
    pass


class DestinyBucketNotFound(DestinyException):
    pass


class DestinyCharacterNotInTower(DestinyException):
    pass


class DestinyCharacterNotLoggedIn(DestinyException):
    pass


class DestinyDefinitionsNotLoaded(DestinyException):
    pass


class DestinyInventoryFull(DestinyException):
    pass


class DestinyItemFailedLevelCheck(DestinyException):
    pass


class DestinyItemFailedUnlockCheck(DestinyException):
    pass


class DestinyItemUnequippable(DestinyException):
    pass


class DestinyItemUniqueEquipRestricted(DestinyException):
    pass


class DestinyNoRoomInDestination(DestinyException):
    pass


class DestinyServiceFailure(DestinyException):
    pass


class DestinyServiceRetired(DestinyException):
    pass


class DestinyTransferFailed(DestinyException):
    pass


class DestinyTransferNotFoundForSourceBucket(DestinyException):
    pass


class DestinyUnexpectedResultInVendorTransferCheck(DestinyException):
    pass


class DestinyUniquenessViolation(DestinyException):
    pass


class DestinyErrorDeserializationFailure(DestinyException):
    pass


class DestinyValidAccountTicketRequired(DestinyException):
    pass


class DestinyShardRelayClientTimeout(DestinyException):
    pass


class DestinyShardRelayProxyTimeout(DestinyException):
    pass


class DestinyPGCRNotFound(DestinyException):
    pass


class DestinyAccountMustBeOffline(DestinyException):
    pass


class DestinyCanOnlyEquipInGame(DestinyException):
    pass


class DestinyCannotPerformActionOnEquippedItem(DestinyException):
    pass


class DestinyQuestAlreadyCompleted(DestinyException):
    pass


class DestinyQuestAlreadyTracked(DestinyException):
    pass


class DestinyTrackableQuestsFull(DestinyException):
    pass


class DestinyItemNotTransferrable(DestinyException):
    pass


class DestinyVendorPurchaseNotAllowed(DestinyException):
    pass


class DestinyContentVersionMismatch(DestinyException):
    pass


class DestinyItemActionForbidden(DestinyException):
    pass


class DestinyRefundInvalid(DestinyException):
    pass


class DestinyPrivacyRestriction(DestinyException):
    pass


class DestinyActionInsufficientPrivileges(DestinyException):
    pass


class DestinyInvalidClaimException(DestinyException):
    pass


class DestinyLegacyPlatformRestricted(DestinyException):
    pass


class DestinyLegacyPlatformInUse(DestinyException):
    pass


class DestinyLegacyPlatformInaccessible(DestinyException):
    pass


class DestinyCannotPerformActionAtThisLocation(DestinyException):
    pass


class DestinyThrottledByGameServer(DestinyException):
    pass


class DestinyItemNotTransferrableHasSideEffects(DestinyException):
    pass


class DestinyItemLocked(DestinyException):
    pass


class DestinyCannotAffordMaterialRequirements(DestinyException):
    pass


class DestinyFailedPlugInsertionRules(DestinyException):
    pass


class DestinySocketNotFound(DestinyException):
    pass


class DestinySocketActionNotAllowed(DestinyException):
    pass


class DestinySocketAlreadyHasPlug(DestinyException):
    pass


class DestinyPlugItemNotAvailable(DestinyException):
    pass


class DestinyCharacterLoggedInNotAllowed(DestinyException):
    pass


class DestinyPublicAccountNotAccessible(DestinyException):
    pass


class DestinyClaimsItemAlreadyClaimed(DestinyException):
    pass


class DestinyClaimsNoInventorySpace(DestinyException):
    pass


class DestinyClaimsRequiredLevelNotMet(DestinyException):
    pass


class DestinyClaimsInvalidState(DestinyException):
    pass


class DestinyNotEnoughRoomForMultipleRewards(DestinyException):
    pass


class DestinyDirectBabelClientTimeout(DestinyException):
    pass


class FbInvalidRequest(DestinyException):
    pass


class FbRedirectMismatch(DestinyException):
    pass


class FbAccessDenied(DestinyException):
    pass


class FbUnsupportedResponseType(DestinyException):
    pass


class FbInvalidScope(DestinyException):
    pass


class FbUnsupportedGrantType(DestinyException):
    pass


class FbInvalidGrant(DestinyException):
    pass


class InvitationExpired(DestinyException):
    pass


class InvitationUnknownType(DestinyException):
    pass


class InvitationInvalidResponseStatus(DestinyException):
    pass


class InvitationInvalidType(DestinyException):
    pass


class InvitationAlreadyPending(DestinyException):
    pass


class InvitationInsufficientPermission(DestinyException):
    pass


class InvitationInvalidCode(DestinyException):
    pass


class InvitationInvalidTargetState(DestinyException):
    pass


class InvitationCannotBeReactivated(DestinyException):
    pass


class InvitationNoRecipients(DestinyException):
    pass


class InvitationGroupCannotSendToSelf(DestinyException):
    pass


class InvitationTooManyRecipients(DestinyException):
    pass


class InvitationInvalid(DestinyException):
    pass


class InvitationNotFound(DestinyException):
    pass


class TokenInvalid(DestinyException):
    pass


class TokenBadFormat(DestinyException):
    pass


class TokenAlreadyClaimed(DestinyException):
    pass


class TokenAlreadyClaimedSelf(DestinyException):
    pass


class TokenThrottling(DestinyException):
    pass


class TokenUnknownRedemptionFailure(DestinyException):
    pass


class TokenPurchaseClaimFailedAfterTokenClaimed(DestinyException):
    pass


class TokenUserAlreadyOwnsOffer(DestinyException):
    pass


class TokenInvalidOfferKey(DestinyException):
    pass


class TokenEmailNotValidated(DestinyException):
    pass


class TokenProvisioningBadVendorOrOffer(DestinyException):
    pass


class TokenPurchaseHistoryUnknownError(DestinyException):
    pass


class TokenThrottleStateUnknownError(DestinyException):
    pass


class TokenUserAgeNotVerified(DestinyException):
    pass


class TokenExceededOfferMaximum(DestinyException):
    pass


class TokenNoAvailableUnlocks(DestinyException):
    pass


class TokenMarketplaceInvalidPlatform(DestinyException):
    pass


class TokenNoMarketplaceCodesFound(DestinyException):
    pass


class TokenOfferNotAvailableForRedemption(DestinyException):
    pass


class TokenUnlockPartialFailure(DestinyException):
    pass


class TokenMarketplaceInvalidRegion(DestinyException):
    pass


class TokenOfferExpired(DestinyException):
    pass


class RAFExceededMaximumReferrals(DestinyException):
    pass


class RAFDuplicateBond(DestinyException):
    pass


class RAFNoValidVeteranDestinyMembershipsFound(DestinyException):
    pass


class RAFNotAValidVeteranUser(DestinyException):
    pass


class RAFCodeAlreadyClaimedOrNotFound(DestinyException):
    pass


class RAFMismatchedDestinyMembershipType(DestinyException):
    pass


class RAFUnableToAccessPurchaseHistory(DestinyException):
    pass


class RAFUnableToCreateBond(DestinyException):
    pass


class RAFUnableToFindBond(DestinyException):
    pass


class RAFUnableToRemoveBond(DestinyException):
    pass


class RAFCannotBondToSelf(DestinyException):
    pass


class RAFInvalidPlatform(DestinyException):
    pass


class RAFGenerateThrottled(DestinyException):
    pass


class RAFUnableToCreateBondVersionMismatch(DestinyException):
    pass


class RAFUnableToRemoveBondVersionMismatch(DestinyException):
    pass


class RAFRedeemThrottled(DestinyException):
    pass


class NoAvailableDiscountCode(DestinyException):
    pass


class DiscountAlreadyClaimed(DestinyException):
    pass


class DiscountClaimFailure(DestinyException):
    pass


class DiscountConfigurationFailure(DestinyException):
    pass


class DiscountGenerationFailure(DestinyException):
    pass


class DiscountAlreadyExists(DestinyException):
    pass


class TokenRequiresCredentialXuid(DestinyException):
    pass


class TokenRequiresCredentialPsnid(DestinyException):
    pass


class OfferRequired(DestinyException):
    pass


class UnknownEververseHistoryError(DestinyException):
    pass


class MissingEververseHistoryError(DestinyException):
    pass


class BungieRewardEmailStateInvalid(DestinyException):
    pass


class BungieRewardNotYetClaimable(DestinyException):
    pass


class MissingOfferConfig(DestinyException):
    pass


class RAFQuestEntitlementRequiresBnet(DestinyException):
    pass


class RAFQuestEntitlementTransportFailure(DestinyException):
    pass


class RAFQuestEntitlementUnknownFailure(DestinyException):
    pass


class RAFVeteranRewardUnknownFailure(DestinyException):
    pass


class RAFTooEarlyToCancelBond(DestinyException):
    pass


class LoyaltyRewardAlreadyRedeemed(DestinyException):
    pass


class UnclaimedLoyaltyRewardEntryNotFound(DestinyException):
    pass


class PartnerOfferPartialFailure(DestinyException):
    pass


class PartnerOfferAlreadyClaimed(DestinyException):
    pass


class PartnerOfferSkuNotFound(DestinyException):
    pass


class PartnerOfferSkuExpired(DestinyException):
    pass


class PartnerOfferPermissionFailure(DestinyException):
    pass


class PartnerOfferNoDestinyAccount(DestinyException):
    pass


class PartnerOfferApplyDataNotFound(DestinyException):
    pass


class ApiExceededMaxKeys(DestinyException):
    pass


class ApiInvalidOrExpiredKey(DestinyException):
    pass


class ApiKeyMissingFromRequest(DestinyException):
    pass


class ApplicationDisabled(DestinyException):
    pass


class ApplicationExceededMax(DestinyException):
    pass


class ApplicationDisallowedByScope(DestinyException):
    pass


class AuthorizationCodeInvalid(DestinyException):
    pass


class OriginHeaderDoesNotMatchKey(DestinyException):
    pass


class AccessNotPermittedByApplicationScope(DestinyException):
    pass


class ApplicationNameIsTaken(DestinyException):
    pass


class RefreshTokenNotYetValid(DestinyException):
    pass


class AccessTokenHasExpired(DestinyException):
    pass


class ApplicationTokenFormatNotValid(DestinyException):
    pass


class ApplicationNotConfiguredForBungieAuth(DestinyException):
    pass


class ApplicationNotConfiguredForOAuth(DestinyException):
    pass


class OAuthAccessTokenExpired(DestinyException):
    pass


class ApplicationTokenKeyIdDoesNotExist(DestinyException):
    pass


class ProvidedTokenNotValidRefreshToken(DestinyException):
    pass


class RefreshTokenExpired(DestinyException):
    pass


class AuthorizationRecordInvalid(DestinyException):
    pass


class TokenPreviouslyRevoked(DestinyException):
    pass


class TokenInvalidMembership(DestinyException):
    pass


class AuthorizationCodeStale(DestinyException):
    pass


class AuthorizationRecordExpired(DestinyException):
    pass


class AuthorizationRecordRevoked(DestinyException):
    pass


class AuthorizationRecordInactiveApiKey(DestinyException):
    pass


class AuthorizationRecordApiKeyMatching(DestinyException):
    pass


class PartnershipInvalidType(DestinyException):
    pass


class PartnershipValidationError(DestinyException):
    pass


class PartnershipValidationTimeout(DestinyException):
    pass


class PartnershipAccessFailure(DestinyException):
    pass


class PartnershipAccountInvalid(DestinyException):
    pass


class PartnershipGetAccountInfoFailure(DestinyException):
    pass


class PartnershipDisabled(DestinyException):
    pass


class PartnershipAlreadyExists(DestinyException):
    pass


class CommunityStreamingUnavailable(DestinyException):
    pass


class TwitchNotLinked(DestinyException):
    pass


class TwitchAccountNotFound(DestinyException):
    pass


class TwitchCouldNotLoadDestinyInfo(DestinyException):
    pass


class TwitchCouldNotRegisterUser(DestinyException):
    pass


class TwitchCouldNotUnregisterUser(DestinyException):
    pass


class TwitchRequiresRelinking(DestinyException):
    pass


class TwitchNoPlatformChosen(DestinyException):
    pass


class TrendingCategoryNotFound(DestinyException):
    pass


class TrendingEntryTypeNotSupported(DestinyException):
    pass


class ReportOffenderNotInPgcr(DestinyException):
    pass


class ReportRequestorNotInPgcr(DestinyException):
    pass


class ReportSubmissionFailed(DestinyException):
    pass


class ReportCannotReportSelf(DestinyException):
    pass


class AwaTypeDisabled(DestinyException):
    pass


class AwaTooManyPendingRequests(DestinyException):
    pass


class AwaTheFeatureRequiresARegisteredDevice(DestinyException):
    pass


class AwaRequestWasUnansweredForTooLong(DestinyException):
    pass


class AwaWriteRequestMissingOrInvalidToken(DestinyException):
    pass


class AwaWriteRequestTokenExpired(DestinyException):
    pass


class AwaWriteRequestTokenUsageLimitReached(DestinyException):
    pass


class SteamWebApiError(DestinyException):
    pass


class SteamWebNullResponseError(DestinyException):
    pass


class SteamAccountRequired(DestinyException):
    pass


class SteamNotAuthorized(DestinyException):
    pass


class ClanFireteamNotFound(DestinyException):
    pass


class ClanFireteamAddNoAlternatesForImmediate(DestinyException):
    pass


class ClanFireteamFull(DestinyException):
    pass


class ClanFireteamAltFull(DestinyException):
    pass


class ClanFireteamBlocked(DestinyException):
    pass


class ClanFireteamPlayerEntryNotFound(DestinyException):
    pass


class ClanFireteamPermissions(DestinyException):
    pass


class ClanFireteamInvalidPlatform(DestinyException):
    pass


class ClanFireteamCannotAdjustSlotCount(DestinyException):
    pass


class ClanFireteamInvalidPlayerPlatform(DestinyException):
    pass


class ClanFireteamNotReadyForInvitesNotEnoughPlayers(DestinyException):
    pass


class ClanFireteamGameInvitesNotSupportForPlatform(DestinyException):
    pass


class ClanFireteamPlatformInvitePreqFailure(DestinyException):
    pass


class ClanFireteamInvalidAuthContext(DestinyException):
    pass


class ClanFireteamInvalidAuthProviderPsn(DestinyException):
    pass


class ClanFireteamPs4SessionFull(DestinyException):
    pass


class ClanFireteamInvalidAuthToken(DestinyException):
    pass


class ClanFireteamScheduledFireteamsDisabled(DestinyException):
    pass


class ClanFireteamNotReadyForInvitesNotScheduledYet(DestinyException):
    pass


class ClanFireteamNotReadyForInvitesClosed(DestinyException):
    pass


class ClanFireteamScheduledFireteamsRequireAdminPermissions(DestinyException):
    pass


class ClanFireteamNonPublicMustHaveClan(DestinyException):
    pass


class ClanFireteamPublicCreationRestriction(DestinyException):
    pass


class ClanFireteamAlreadyJoined(DestinyException):
    pass


class ClanFireteamScheduledFireteamsRange(DestinyException):
    pass


class ClanFireteamPublicCreationRestrictionExtended(DestinyException):
    pass


class ClanFireteamExpired(DestinyException):
    pass


class ClanFireteamInvalidAuthProvider(DestinyException):
    pass


class ClanFireteamInvalidAuthProviderXuid(DestinyException):
    pass


class ClanFireteamThrottle(DestinyException):
    pass


class ClanFireteamTooManyOpenScheduledFireteams(DestinyException):
    pass


class ClanFireteamCannotReopenScheduledFireteams(DestinyException):
    pass


class ClanFireteamJoinNoAccountSpecified(DestinyException):
    pass


class ClanFireteamMinDestiny2ProgressForCreation(DestinyException):
    pass


class ClanFireteamMinDestiny2ProgressForJoin(DestinyException):
    pass


class ClanFireteamSMSOrPurchaseRequiredCreate(DestinyException):
    pass


class ClanFireteamPurchaseRequiredCreate(DestinyException):
    pass


class ClanFireteamSMSOrPurchaseRequiredJoin(DestinyException):
    pass


class ClanFireteamPurchaseRequiredJoin(DestinyException):
    pass


class CrossSaveOverriddenAccountNotFound(DestinyException):
    pass


class CrossSaveTooManyOverriddenPlatforms(DestinyException):
    pass


class CrossSaveNoOverriddenPlatforms(DestinyException):
    pass


class CrossSavePrimaryAccountNotFound(DestinyException):
    pass


class CrossSaveRequestInvalid(DestinyException):
    pass


class CrossSaveBungieAccountValidationFailure(DestinyException):
    pass


class CrossSaveOverriddenPlatformNotAllowed(DestinyException):
    pass


class CrossSaveThresholdExceeded(DestinyException):
    pass


class CrossSaveIncompatibleMembershipType(DestinyException):
    pass


class CrossSaveCouldNotFindLinkedAccountForMembershipType(DestinyException):
    pass


class CrossSaveCouldNotCreateDestinyProfileForMembershipType(DestinyException):
    pass


class CrossSaveErrorCreatingDestinyProfileForMembershipType(DestinyException):
    pass


class CrossSaveCannotOverrideSelf(DestinyException):
    pass


class CrossSaveRecentSilverPurchase(DestinyException):
    pass


class CrossSaveSilverBalanceNegative(DestinyException):
    pass


class CrossSaveAccountNotAuthenticated(DestinyException):
    pass


class ErrorOneAccountAlreadyActive(DestinyException):
    pass


class ErrorOneAccountDestinyRestriction(DestinyException):
    pass


class CrossSaveMustMigrateToSteam(DestinyException):
    pass


class CrossSaveSteamAlreadyPaired(DestinyException):
    pass


class CrossSaveCannotPairJustSteamAndBlizzard(DestinyException):
    pass


class CrossSaveCannotPairSteamAloneBeforeShadowkeep(DestinyException):
    pass


class AuthVerificationNotLinkedToAccount(DestinyException):
    pass


class PCMigrationMissingBlizzard(DestinyException):
    pass


class PCMigrationMissingSteam(DestinyException):
    pass


class PCMigrationInvalidBlizzard(DestinyException):
    pass


class PCMigrationInvalidSteam(DestinyException):
    pass


class PCMigrationUnknownFailure(DestinyException):
    pass


class PCMigrationUnknownException(DestinyException):
    pass


class PCMigrationNotLinked(DestinyException):
    pass


class PCMigrationAccountsAlreadyUsed(DestinyException):
    pass


class PCMigrationStepFailed(DestinyException):
    pass


class PCMigrationInvalidBlizzardCrossSaveState(DestinyException):
    pass


class PCMigrationDestinationBanned(DestinyException):
    pass


class PCMigrationDestinyFailure(DestinyException):
    pass


class PCMigrationSilverTransferFailed(DestinyException):
    pass


class PCMigrationEntitlementTransferFailed(DestinyException):
    pass


class PCMigrationCannotStompClanFounder(DestinyException):
    pass


class UnsupportedBrowser(DestinyException):
    pass


class StadiaAccountRequired(DestinyException):
    pass


class ErrorPhoneValidationTooManyUses(DestinyException):
    pass


class ErrorPhoneValidationNoAssociatedPhone(DestinyException):
    pass


class ErrorPhoneValidationCodeInvalid(DestinyException):
    pass


class ErrorPhoneValidationBanned(DestinyException):
    pass


class ErrorPhoneValidationCodeTooRecentlySent(DestinyException):
    pass


class ErrorPhoneValidationCodeExpired(DestinyException):
    pass


class ErrorPhoneValidationInvalidNumberType(DestinyException):
    pass


class ErrorPhoneValidationCodeTooRecentlyChecked(DestinyException):
    pass


class ApplePushErrorUnknown(DestinyException):
    pass


class ApplePushErrorNull(DestinyException):
    pass


class ApplePushErrorTimeout(DestinyException):
    pass


class ApplePushBadRequest(DestinyException):
    pass


class ApplePushFailedAuth(DestinyException):
    pass


class ApplePushThrottled(DestinyException):
    pass


class ApplePushServiceUnavailable(DestinyException):
    pass


class NotAnImageOrVideo(DestinyException):
    pass


class ErrorBungieFriendsBlockFailed(DestinyException):
    pass


class ErrorBungieFriendsAutoReject(DestinyException):
    pass


class ErrorBungieFriendsNoRequestFound(DestinyException):
    pass


class ErrorBungieFriendsAlreadyFriends(DestinyException):
    pass


class ErrorBungieFriendsUnableToRemoveRequest(DestinyException):
    pass


class ErrorBungieFriendsUnableToRemove(DestinyException):
    pass


class ErrorBungieFriendsIdenticalSourceTarget(DestinyException):
    pass


class ErrorBungieFriendsSelf(DestinyException):
    pass


class ErrorBungieBlockSelf(DestinyException):
    pass


class ErrorBungieFriendsListFull(DestinyException):
    pass


class ErrorBungieBlockListFull(DestinyException):
    pass


EXCEPTIONS = {
    0: None_,
    1: Success,
    2: TransportException,
    3: UnhandledException,
    4: NotImplemented,
    5: SystemDisabled,
    6: FailedToLoadAvailableLocalesConfiguration,
    7: ParameterParseFailure,
    8: ParameterInvalidRange,
    9: BadRequest,
    10: AuthenticationInvalid,
    11: DataNotFound,
    12: InsufficientPrivileges,
    13: Duplicate,
    14: UnknownSqlResult,
    15: ValidationError,
    16: ValidationMissingFieldError,
    17: ValidationInvalidInputError,
    18: InvalidParameters,
    19: ParameterNotFound,
    20: UnhandledHttpException,
    21: NotFound,
    22: WebAuthModuleAsyncFailed,
    23: InvalidReturnValue,
    24: UserBanned,
    25: InvalidPostBody,
    26: MissingPostBody,
    27: ExternalServiceTimeout,
    28: ValidationLengthError,
    29: ValidationRangeError,
    30: JsonDeserializationError,
    31: ThrottleLimitExceeded,
    32: ValidationTagError,
    33: ValidationProfanityError,
    34: ValidationUrlFormatError,
    35: ThrottleLimitExceededMinutes,
    36: ThrottleLimitExceededMomentarily,
    37: ThrottleLimitExceededSeconds,
    38: ExternalServiceUnknown,
    39: ValidationWordLengthError,
    40: ValidationInvisibleUnicode,
    41: ValidationBadNames,
    42: ExternalServiceFailed,
    43: ServiceRetired,
    44: UnknownSqlException,
    45: UnsupportedLocale,
    46: InvalidPageNumber,
    47: MaximumPageSizeExceeded,
    48: ServiceUnsupported,
    49: ValidationMaximumUnicodeCombiningCharacters,
    50: ValidationMaximumSequentialCarriageReturns,
    51: PerEndpointRequestThrottleExceeded,
    52: AuthContextCacheAssertion,
    53: ExPlatformStringValidationError,
    54: PerApplicationThrottleExceeded,
    55: PerApplicationAnonymousThrottleExceeded,
    56: PerApplicationAuthenticatedThrottleExceeded,
    57: PerUserThrottleExceeded,
    58: PayloadSignatureVerificationFailure,
    59: InvalidServiceAuthContext,
    89: ObsoleteCredentialType,
    90: UnableToUnPairMobileApp,
    91: UnableToPairMobileApp,
    92: CannotUseMobileAuthWithNonMobileProvider,
    93: MissingDeviceCookie,
    94: FacebookTokenExpired,
    95: AuthTicketRequired,
    96: CookieContextRequired,
    97: UnknownAuthenticationError,
    98: BungieNetAccountCreationRequired,
    99: WebAuthRequired,
    100: ContentUnknownSqlResult,
    101: ContentNeedUniquePath,
    102: ContentSqlException,
    103: ContentNotFound,
    104: ContentSuccessWithTagAddFail,
    105: ContentSearchMissingParameters,
    106: ContentInvalidId,
    107: ContentPhysicalFileDeletionError,
    108: ContentPhysicalFileCreationError,
    109: ContentPerforceSubmissionError,
    110: ContentPerforceInitializationError,
    111: ContentDeploymentPackageNotReadyError,
    112: ContentUploadFailed,
    113: ContentTooManyResults,
    115: ContentInvalidState,
    116: ContentNavigationParentNotFound,
    117: ContentNavigationParentUpdateError,
    118: DeploymentPackageNotEditable,
    119: ContentValidationError,
    120: ContentPropertiesValidationError,
    121: ContentTypeNotFound,
    122: DeploymentPackageNotFound,
    123: ContentSearchInvalidParameters,
    124: ContentItemPropertyAggregationError,
    125: DeploymentPackageFileNotFound,
    126: ContentPerforceFileHistoryNotFound,
    127: ContentAssetZipCreationFailure,
    128: ContentAssetZipCreationBusy,
    129: ContentProjectNotFound,
    130: ContentFolderNotFound,
    131: ContentPackagesInconsistent,
    132: ContentPackagesInvalidState,
    133: ContentPackagesInconsistentType,
    134: ContentCannotDeletePackage,
    135: ContentLockedForChanges,
    136: ContentFileUploadFailed,
    137: ContentNotReviewed,
    138: ContentPermissionDenied,
    139: ContentInvalidExternalUrl,
    140: ContentExternalFileCannotBeImportedLocally,
    141: ContentTagSaveFailure,
    142: ContentPerforceUnmatchedFileError,
    143: ContentPerforceChangelistResultNotFound,
    144: ContentPerforceChangelistFileItemsNotFound,
    145: ContentPerforceInvalidRevisionError,
    146: ContentUnloadedSaveResult,
    147: ContentPropertyInvalidNumber,
    148: ContentPropertyInvalidUrl,
    149: ContentPropertyInvalidDate,
    150: ContentPropertyInvalidSet,
    151: ContentPropertyCannotDeserialize,
    152: ContentRegexValidationFailOnProperty,
    153: ContentMaxLengthFailOnProperty,
    154: ContentPropertyUnexpectedDeserializationError,
    155: ContentPropertyRequired,
    156: ContentCannotCreateFile,
    157: ContentInvalidMigrationFile,
    158: ContentMigrationAlteringProcessedItem,
    159: ContentPropertyDefinitionNotFound,
    160: ContentReviewDataChanged,
    161: ContentRollbackRevisionNotInPackage,
    162: ContentItemNotBasedOnLatestRevision,
    163: ContentUnauthorized,
    164: ContentCannotCreateDeploymentPackage,
    165: ContentUserNotFound,
    166: ContentLocalePermissionDenied,
    167: ContentInvalidLinkToInternalEnvironment,
    168: ContentInvalidBlacklistedContent,
    169: ContentMacroMalformedNoContentId,
    170: ContentMacroMalformedNoTemplateType,
    171: ContentIllegalBNetMembershipId,
    172: ContentLocaleDidNotMatchExpected,
    173: ContentBabelCallFailed,
    174: ContentEnglishPostLiveForbidden,
    175: ContentLocaleEditPermissionDenied,
    200: UserNonUniqueName,
    201: UserManualLinkingStepRequired,
    202: UserCreateUnknownSqlResult,
    203: UserCreateUnknownSqlException,
    204: UserMalformedMembershipId,
    205: UserCannotFindRequestedUser,
    206: UserCannotLoadAccountCredentialLinkInfo,
    207: UserInvalidMobileAppType,
    208: UserMissingMobilePairingInfo,
    209: UserCannotGenerateMobileKeyWhileUsingMobileCredential,
    210: UserGenerateMobileKeyExistingSlotCollision,
    211: UserDisplayNameMissingOrInvalid,
    212: UserCannotLoadAccountProfileData,
    213: UserCannotSaveUserProfileData,
    214: UserEmailMissingOrInvalid,
    215: UserTermsOfUseRequired,
    216: UserCannotCreateNewAccountWhileLoggedIn,
    217: UserCannotResolveCentralAccount,
    218: UserInvalidAvatar,
    219: UserMissingCreatedUserResult,
    220: UserCannotChangeUniqueNameYet,
    221: UserCannotChangeDisplayNameYet,
    222: UserCannotChangeEmail,
    223: UserUniqueNameMustStartWithLetter,
    224: UserNoLinkedAccountsSupportFriendListings,
    225: UserAcknowledgmentTableFull,
    226: UserCreationDestinyMembershipRequired,
    227: UserFriendsTokenNeedsRefresh,
    228: UserEmailValidationUnknown,
    229: UserEmailValidationLimit,
    230: TransactionEmailSendFailure,
    231: MailHookPermissionFailure,
    232: MailServiceRateLimit,
    233: UserEmailMustBeVerified,
    234: UserMustAllowCustomerServiceEmails,
    235: NonTransactionalEmailSendFailure,
    236: UnknownErrorSettingGlobalDisplayName,
    237: DuplicateGlobalDisplayName,
    238: ErrorRunningNameValidationChecks,
    239: ErrorDatabaseGlobalName,
    240: ErrorNoAvailableNameChanges,
    241: ErrorNameAlreadySetToInput,
    300: MessagingUnknownError,
    301: MessagingSelfError,
    302: MessagingSendThrottle,
    303: MessagingNoBody,
    304: MessagingTooManyUsers,
    305: MessagingCanNotLeaveConversation,
    306: MessagingUnableToSend,
    307: MessagingDeletedUserForbidden,
    308: MessagingCannotDeleteExternalConversation,
    309: MessagingGroupChatDisabled,
    310: MessagingMustIncludeSelfInPrivateMessage,
    311: MessagingSenderIsBanned,
    312: MessagingGroupOptionalChatExceededMaximum,
    313: PrivateMessagingRequiresDestinyMembership,
    400: AddSurveyAnswersUnknownSqlException,
    500: ForumBodyCannotBeEmpty,
    501: ForumSubjectCannotBeEmptyOnTopicPost,
    502: ForumCannotLocateParentPost,
    503: ForumThreadLockedForReplies,
    504: ForumUnknownSqlResultDuringCreatePost,
    505: ForumUnknownTagCreationError,
    506: ForumUnknownSqlResultDuringTagItem,
    507: ForumUnknownExceptionCreatePost,
    508: ForumQuestionMustBeTopicPost,
    509: ForumExceptionDuringTagSearch,
    510: ForumExceptionDuringTopicRetrieval,
    511: ForumAliasedTagError,
    512: ForumCannotLocateThread,
    513: ForumUnknownExceptionEditPost,
    514: ForumCannotLocatePost,
    515: ForumUnknownExceptionGetOrCreateTags,
    516: ForumEditPermissionDenied,
    517: ForumUnknownSqlResultDuringTagIdRetrieval,
    518: ForumCannotGetRating,
    519: ForumUnknownExceptionGetRating,
    520: ForumRatingsAccessError,
    521: ForumRelatedPostAccessError,
    522: ForumLatestReplyAccessError,
    523: ForumUserStatusAccessError,
    524: ForumAuthorAccessError,
    525: ForumGroupAccessError,
    526: ForumUrlExpectedButMissing,
    527: ForumRepliesCannotBeEmpty,
    528: ForumRepliesCannotBeInDifferentGroups,
    529: ForumSubTopicCannotBeCreatedAtThisThreadLevel,
    530: ForumCannotCreateContentTopic,
    531: ForumTopicDoesNotExist,
    532: ForumContentCommentsNotAllowed,
    533: ForumUnknownSqlResultDuringEditPost,
    534: ForumUnknownSqlResultDuringGetPost,
    535: ForumPostValidationBadUrl,
    536: ForumBodyTooLong,
    537: ForumSubjectTooLong,
    538: ForumAnnouncementNotAllowed,
    539: ForumCannotShareOwnPost,
    540: ForumEditNoOp,
    541: ForumUnknownDatabaseErrorDuringGetPost,
    542: ForumExceeedMaximumRowLimit,
    543: ForumCannotSharePrivatePost,
    544: ForumCannotCrossPostBetweenGroups,
    555: ForumIncompatibleCategories,
    556: ForumCannotUseTheseCategoriesOnNonTopicPost,
    557: ForumCanOnlyDeleteTopics,
    558: ForumDeleteSqlException,
    559: ForumDeleteSqlUnknownResult,
    560: ForumTooManyTags,
    561: ForumCanOnlyRateTopics,
    562: ForumBannedPostsCannotBeEdited,
    563: ForumThreadRootIsBanned,
    564: ForumCannotUseOfficialTagCategoryAsTag,
    565: ForumAnswerCannotBeMadeOnCreatePost,
    566: ForumAnswerCannotBeMadeOnEditPost,
    567: ForumAnswerPostIdIsNotADirectReplyOfQuestion,
    568: ForumAnswerTopicIdIsNotAQuestion,
    569: ForumUnknownExceptionDuringMarkAnswer,
    570: ForumUnknownSqlResultDuringMarkAnswer,
    571: ForumCannotRateYourOwnPosts,
    572: ForumPollsMustBeTheFirstPostInTopic,
    573: ForumInvalidPollInput,
    574: ForumGroupAdminEditNonMember,
    575: ForumCannotEditModeratorEditedPost,
    576: ForumRequiresDestinyMembership,
    577: ForumUnexpectedError,
    578: ForumAgeLock,
    579: ForumMaxPages,
    580: ForumMaxPagesOldestFirst,
    581: ForumCannotApplyForumIdWithoutTags,
    582: ForumCannotApplyForumIdToNonTopics,
    583: ForumCannotDownvoteCommunityCreations,
    584: ForumTopicsMustHaveOfficialCategory,
    585: ForumRecruitmentTopicMalformed,
    586: ForumRecruitmentTopicNotFound,
    587: ForumRecruitmentTopicNoSlotsRemaining,
    588: ForumRecruitmentTopicKickBan,
    589: ForumRecruitmentTopicRequirementsNotMet,
    590: ForumRecruitmentTopicNoPlayers,
    591: ForumRecruitmentApproveFailMessageBan,
    592: ForumRecruitmentGlobalBan,
    593: ForumUserBannedFromThisTopic,
    594: ForumRecruitmentFireteamMembersOnly,
    595: ForumRequiresDestiny2Progress,
    601: GroupMembershipApplicationAlreadyResolved,
    602: GroupMembershipAlreadyApplied,
    603: GroupMembershipInsufficientPrivileges,
    604: GroupIdNotReturnedFromCreation,
    605: GroupSearchInvalidParameters,
    606: GroupMembershipPendingApplicationNotFound,
    607: GroupInvalidId,
    608: GroupInvalidMembershipId,
    609: GroupInvalidMembershipType,
    610: GroupMissingTags,
    611: GroupMembershipNotFound,
    612: GroupInvalidRating,
    613: GroupUserFollowingAccessError,
    614: GroupUserMembershipAccessError,
    615: GroupCreatorAccessError,
    616: GroupAdminAccessError,
    617: GroupPrivatePostNotViewable,
    618: GroupMembershipNotLoggedIn,
    619: GroupNotDeleted,
    620: GroupUnknownErrorUndeletingGroup,
    621: GroupDeleted,
    622: GroupNotFound,
    623: GroupMemberBanned,
    624: GroupMembershipClosed,
    625: GroupPrivatePostOverrideError,
    626: GroupNameTaken,
    627: GroupDeletionGracePeriodExpired,
    628: GroupCannotCheckBanStatus,
    629: GroupMaximumMembershipCountReached,
    630: NoDestinyAccountForClanPlatform,
    631: AlreadyRequestingMembershipForClanPlatform,
    632: AlreadyClanMemberOnPlatform,
    633: GroupJoinedCannotSetClanName,
    634: GroupLeftCannotClearClanName,
    635: GroupRelationshipRequestPending,
    636: GroupRelationshipRequestBlocked,
    637: GroupRelationshipRequestNotFound,
    638: GroupRelationshipBlockNotFound,
    639: GroupRelationshipNotFound,
    641: GroupAlreadyAllied,
    642: GroupAlreadyMember,
    643: GroupRelationshipAlreadyExists,
    644: InvalidGroupTypesForRelationshipRequest,
    646: GroupAtMaximumAlliances,
    647: GroupCannotSetClanOnlySettings,
    648: ClanCannotSetTwoDefaultPostTypes,
    649: GroupMemberInvalidMemberType,
    650: GroupInvalidPlatformType,
    651: GroupMemberInvalidSort,
    652: GroupInvalidResolveState,
    653: ClanAlreadyEnabledForPlatform,
    654: ClanNotEnabledForPlatform,
    655: ClanEnabledButCouldNotJoinNoAccount,
    656: ClanEnabledButCouldNotJoinAlreadyMember,
    657: ClanCannotJoinNoCredential,
    658: NoClanMembershipForPlatform,
    659: GroupToGroupFollowLimitReached,
    660: ChildGroupAlreadyInAlliance,
    661: OwnerGroupAlreadyInAlliance,
    662: AllianceOwnerCannotJoinAlliance,
    663: GroupNotInAlliance,
    664: ChildGroupCannotInviteToAlliance,
    665: GroupToGroupAlreadyFollowed,
    666: GroupToGroupNotFollowing,
    667: ClanMaximumMembershipReached,
    668: ClanNameNotValid,
    669: ClanNameNotValidError,
    670: AllianceOwnerNotDefined,
    671: AllianceChildNotDefined,
    672: ClanCultureIllegalCharacters,
    673: ClanTagIllegalCharacters,
    674: ClanRequiresInvitation,
    675: ClanMembershipClosed,
    676: ClanInviteAlreadyMember,
    677: GroupInviteAlreadyMember,
    678: GroupJoinApprovalRequired,
    679: ClanTagRequired,
    680: GroupNameCannotStartOrEndWithWhiteSpace,
    681: ClanCallsignCannotStartOrEndWithWhiteSpace,
    682: ClanMigrationFailed,
    683: ClanNotEnabledAlreadyMemberOfAnotherClan,
    684: GroupModerationNotPermittedOnNonMembers,
    685: ClanCreationInWorldServerFailed,
    686: ClanNotFound,
    687: ClanMembershipLevelDoesNotPermitThatAction,
    688: ClanMemberNotFound,
    689: ClanMissingMembershipApprovers,
    690: ClanInWrongStateForRequestedAction,
    691: ClanNameAlreadyUsed,
    692: ClanTooFewMembers,
    693: ClanInfoCannotBeWhitespace,
    694: GroupCultureThrottle,
    695: ClanTargetDisallowsInvites,
    696: ClanInvalidOperation,
    697: ClanFounderCannotLeaveWithoutAbdication,
    698: ClanNameReserved,
    699: ClanApplicantInClanSoNowInvited,
    701: ActivitiesUnknownException,
    702: ActivitiesParameterNull,
    703: ActivityCountsDiabled,
    704: ActivitySearchInvalidParameters,
    705: ActivityPermissionDenied,
    706: ShareAlreadyShared,
    707: ActivityLoggingDisabled,
    750: ClanRequiresExistingDestinyAccount,
    751: ClanNameRestricted,
    752: ClanCreationBan,
    753: ClanCreationTenureRequirementsNotMet,
    801: ItemAlreadyFollowed,
    802: ItemNotFollowed,
    803: CannotFollowSelf,
    804: GroupFollowLimitExceeded,
    805: TagFollowLimitExceeded,
    806: UserFollowLimitExceeded,
    807: FollowUnsupportedEntityType,
    900: NoValidTagsInList,
    901: BelowMinimumSuggestionLength,
    902: CannotGetSuggestionsOnMultipleTagsSimultaneously,
    903: NotAValidPartialTag,
    904: TagSuggestionsUnknownSqlResult,
    905: TagsUnableToLoadPopularTagsFromDatabase,
    906: TagInvalid,
    907: TagNotFound,
    908: SingleTagExpected,
    909: TagsExceededMaximumPerItem,
    1000: IgnoreInvalidParameters,
    1001: IgnoreSqlException,
    1002: IgnoreErrorRetrievingGroupPermissions,
    1003: IgnoreErrorInsufficientPermission,
    1004: IgnoreErrorRetrievingItem,
    1005: IgnoreCannotIgnoreSelf,
    1006: IgnoreIllegalType,
    1007: IgnoreNotFound,
    1008: IgnoreUserGloballyIgnored,
    1009: IgnoreUserIgnored,
    1010: TargetUserIgnored,
    1100: NotificationSettingInvalid,
    1204: PsnApiExpiredAccessToken,
    1205: PSNExForbidden,
    1218: PSNExSystemDisabled,
    1223: PsnApiErrorCodeUnknown,
    1224: PsnApiErrorWebException,
    1225: PsnApiBadRequest,
    1226: PsnApiAccessTokenRequired,
    1227: PsnApiInvalidAccessToken,
    1229: PsnApiBannedUser,
    1230: PsnApiAccountUpgradeRequired,
    1231: PsnApiServiceTemporarilyUnavailable,
    1232: PsnApiServerBusy,
    1233: PsnApiUnderMaintenance,
    1234: PsnApiProfileUserNotFound,
    1235: PsnApiProfilePrivacyRestriction,
    1236: PsnApiProfileUnderMaintenance,
    1237: PsnApiAccountAttributeMissing,
    1238: PsnApiNoPermission,
    1239: PsnApiTargetUserBlocked,
    1240: PsnApiJwksMissing,
    1241: PsnApiJwtMalformedHeader,
    1242: PsnApiJwtMalformedPayload,
    1300: XblExSystemDisabled,
    1301: XblExUnknownError,
    1302: XblApiErrorWebException,
    1303: XblStsTokenInvalid,
    1304: XblStsMissingToken,
    1305: XblStsExpiredToken,
    1306: XblAccessToTheSandboxDenied,
    1307: XblMsaResponseMissing,
    1308: XblMsaAccessTokenExpired,
    1309: XblMsaInvalidRequest,
    1310: XblMsaFriendsRequireSignIn,
    1311: XblUserActionRequired,
    1312: XblParentalControls,
    1313: XblDeveloperAccount,
    1314: XblUserTokenExpired,
    1315: XblUserTokenInvalid,
    1316: XblOffline,
    1317: XblUnknownErrorCode,
    1318: XblMsaInvalidGrant,
    1400: ReportNotYetResolved,
    1401: ReportOverturnDoesNotChangeDecision,
    1402: ReportNotFound,
    1403: ReportAlreadyReported,
    1404: ReportInvalidResolution,
    1405: ReportNotAssignedToYou,
    1500: LegacyGameStatsSystemDisabled,
    1501: LegacyGameStatsUnknownError,
    1502: LegacyGameStatsMalformedSneakerNetCode,
    1600: DestinyAccountAcquisitionFailure,
    1601: DestinyAccountNotFound,
    1602: DestinyBuildStatsDatabaseError,
    1603: DestinyCharacterStatsDatabaseError,
    1604: DestinyPvPStatsDatabaseError,
    1605: DestinyPvEStatsDatabaseError,
    1606: DestinyGrimoireStatsDatabaseError,
    1607: DestinyStatsParameterMembershipTypeParseError,
    1608: DestinyStatsParameterMembershipIdParseError,
    1609: DestinyStatsParameterRangeParseError,
    1610: DestinyStringItemHashNotFound,
    1611: DestinyStringSetNotFound,
    1612: DestinyContentLookupNotFoundForKey,
    1613: DestinyContentItemNotFound,
    1614: DestinyContentSectionNotFound,
    1615: DestinyContentPropertyNotFound,
    1616: DestinyContentConfigNotFound,
    1617: DestinyContentPropertyBucketValueNotFound,
    1618: DestinyUnexpectedError,
    1619: DestinyInvalidAction,
    1620: DestinyCharacterNotFound,
    1621: DestinyInvalidFlag,
    1622: DestinyInvalidRequest,
    1623: DestinyItemNotFound,
    1624: DestinyInvalidCustomizationChoices,
    1625: DestinyVendorItemNotFound,
    1626: DestinyInternalError,
    1627: DestinyVendorNotFound,
    1628: DestinyRecentActivitiesDatabaseError,
    1629: DestinyItemBucketNotFound,
    1630: DestinyInvalidMembershipType,
    1631: DestinyVersionIncompatibility,
    1632: DestinyItemAlreadyInInventory,
    1633: DestinyBucketNotFound,
    1634: DestinyCharacterNotInTower,
    1635: DestinyCharacterNotLoggedIn,
    1636: DestinyDefinitionsNotLoaded,
    1637: DestinyInventoryFull,
    1638: DestinyItemFailedLevelCheck,
    1639: DestinyItemFailedUnlockCheck,
    1640: DestinyItemUnequippable,
    1641: DestinyItemUniqueEquipRestricted,
    1642: DestinyNoRoomInDestination,
    1643: DestinyServiceFailure,
    1644: DestinyServiceRetired,
    1645: DestinyTransferFailed,
    1646: DestinyTransferNotFoundForSourceBucket,
    1647: DestinyUnexpectedResultInVendorTransferCheck,
    1648: DestinyUniquenessViolation,
    1649: DestinyErrorDeserializationFailure,
    1650: DestinyValidAccountTicketRequired,
    1651: DestinyShardRelayClientTimeout,
    1652: DestinyShardRelayProxyTimeout,
    1653: DestinyPGCRNotFound,
    1654: DestinyAccountMustBeOffline,
    1655: DestinyCanOnlyEquipInGame,
    1656: DestinyCannotPerformActionOnEquippedItem,
    1657: DestinyQuestAlreadyCompleted,
    1658: DestinyQuestAlreadyTracked,
    1659: DestinyTrackableQuestsFull,
    1660: DestinyItemNotTransferrable,
    1661: DestinyVendorPurchaseNotAllowed,
    1662: DestinyContentVersionMismatch,
    1663: DestinyItemActionForbidden,
    1664: DestinyRefundInvalid,
    1665: DestinyPrivacyRestriction,
    1666: DestinyActionInsufficientPrivileges,
    1667: DestinyInvalidClaimException,
    1668: DestinyLegacyPlatformRestricted,
    1669: DestinyLegacyPlatformInUse,
    1670: DestinyLegacyPlatformInaccessible,
    1671: DestinyCannotPerformActionAtThisLocation,
    1672: DestinyThrottledByGameServer,
    1673: DestinyItemNotTransferrableHasSideEffects,
    1674: DestinyItemLocked,
    1675: DestinyCannotAffordMaterialRequirements,
    1676: DestinyFailedPlugInsertionRules,
    1677: DestinySocketNotFound,
    1678: DestinySocketActionNotAllowed,
    1679: DestinySocketAlreadyHasPlug,
    1680: DestinyPlugItemNotAvailable,
    1681: DestinyCharacterLoggedInNotAllowed,
    1682: DestinyPublicAccountNotAccessible,
    1683: DestinyClaimsItemAlreadyClaimed,
    1684: DestinyClaimsNoInventorySpace,
    1685: DestinyClaimsRequiredLevelNotMet,
    1686: DestinyClaimsInvalidState,
    1687: DestinyNotEnoughRoomForMultipleRewards,
    1688: DestinyDirectBabelClientTimeout,
    1800: FbInvalidRequest,
    1801: FbRedirectMismatch,
    1802: FbAccessDenied,
    1803: FbUnsupportedResponseType,
    1804: FbInvalidScope,
    1805: FbUnsupportedGrantType,
    1806: FbInvalidGrant,
    1900: InvitationExpired,
    1901: InvitationUnknownType,
    1902: InvitationInvalidResponseStatus,
    1903: InvitationInvalidType,
    1904: InvitationAlreadyPending,
    1905: InvitationInsufficientPermission,
    1906: InvitationInvalidCode,
    1907: InvitationInvalidTargetState,
    1908: InvitationCannotBeReactivated,
    1910: InvitationNoRecipients,
    1911: InvitationGroupCannotSendToSelf,
    1912: InvitationTooManyRecipients,
    1913: InvitationInvalid,
    1914: InvitationNotFound,
    2000: TokenInvalid,
    2001: TokenBadFormat,
    2002: TokenAlreadyClaimed,
    2003: TokenAlreadyClaimedSelf,
    2004: TokenThrottling,
    2005: TokenUnknownRedemptionFailure,
    2006: TokenPurchaseClaimFailedAfterTokenClaimed,
    2007: TokenUserAlreadyOwnsOffer,
    2008: TokenInvalidOfferKey,
    2009: TokenEmailNotValidated,
    2010: TokenProvisioningBadVendorOrOffer,
    2011: TokenPurchaseHistoryUnknownError,
    2012: TokenThrottleStateUnknownError,
    2013: TokenUserAgeNotVerified,
    2014: TokenExceededOfferMaximum,
    2015: TokenNoAvailableUnlocks,
    2016: TokenMarketplaceInvalidPlatform,
    2017: TokenNoMarketplaceCodesFound,
    2018: TokenOfferNotAvailableForRedemption,
    2019: TokenUnlockPartialFailure,
    2020: TokenMarketplaceInvalidRegion,
    2021: TokenOfferExpired,
    2022: RAFExceededMaximumReferrals,
    2023: RAFDuplicateBond,
    2024: RAFNoValidVeteranDestinyMembershipsFound,
    2025: RAFNotAValidVeteranUser,
    2026: RAFCodeAlreadyClaimedOrNotFound,
    2027: RAFMismatchedDestinyMembershipType,
    2028: RAFUnableToAccessPurchaseHistory,
    2029: RAFUnableToCreateBond,
    2030: RAFUnableToFindBond,
    2031: RAFUnableToRemoveBond,
    2032: RAFCannotBondToSelf,
    2033: RAFInvalidPlatform,
    2034: RAFGenerateThrottled,
    2035: RAFUnableToCreateBondVersionMismatch,
    2036: RAFUnableToRemoveBondVersionMismatch,
    2037: RAFRedeemThrottled,
    2038: NoAvailableDiscountCode,
    2039: DiscountAlreadyClaimed,
    2040: DiscountClaimFailure,
    2041: DiscountConfigurationFailure,
    2042: DiscountGenerationFailure,
    2043: DiscountAlreadyExists,
    2044: TokenRequiresCredentialXuid,
    2045: TokenRequiresCredentialPsnid,
    2046: OfferRequired,
    2047: UnknownEververseHistoryError,
    2048: MissingEververseHistoryError,
    2049: BungieRewardEmailStateInvalid,
    2050: BungieRewardNotYetClaimable,
    2051: MissingOfferConfig,
    2052: RAFQuestEntitlementRequiresBnet,
    2053: RAFQuestEntitlementTransportFailure,
    2054: RAFQuestEntitlementUnknownFailure,
    2055: RAFVeteranRewardUnknownFailure,
    2056: RAFTooEarlyToCancelBond,
    2057: LoyaltyRewardAlreadyRedeemed,
    2058: UnclaimedLoyaltyRewardEntryNotFound,
    2059: PartnerOfferPartialFailure,
    2060: PartnerOfferAlreadyClaimed,
    2061: PartnerOfferSkuNotFound,
    2062: PartnerOfferSkuExpired,
    2063: PartnerOfferPermissionFailure,
    2064: PartnerOfferNoDestinyAccount,
    2065: PartnerOfferApplyDataNotFound,
    2100: ApiExceededMaxKeys,
    2101: ApiInvalidOrExpiredKey,
    2102: ApiKeyMissingFromRequest,
    2103: ApplicationDisabled,
    2104: ApplicationExceededMax,
    2105: ApplicationDisallowedByScope,
    2106: AuthorizationCodeInvalid,
    2107: OriginHeaderDoesNotMatchKey,
    2108: AccessNotPermittedByApplicationScope,
    2109: ApplicationNameIsTaken,
    2110: RefreshTokenNotYetValid,
    2111: AccessTokenHasExpired,
    2112: ApplicationTokenFormatNotValid,
    2113: ApplicationNotConfiguredForBungieAuth,
    2114: ApplicationNotConfiguredForOAuth,
    2115: OAuthAccessTokenExpired,
    2116: ApplicationTokenKeyIdDoesNotExist,
    2117: ProvidedTokenNotValidRefreshToken,
    2118: RefreshTokenExpired,
    2119: AuthorizationRecordInvalid,
    2120: TokenPreviouslyRevoked,
    2121: TokenInvalidMembership,
    2122: AuthorizationCodeStale,
    2123: AuthorizationRecordExpired,
    2124: AuthorizationRecordRevoked,
    2125: AuthorizationRecordInactiveApiKey,
    2126: AuthorizationRecordApiKeyMatching,
    2200: PartnershipInvalidType,
    2201: PartnershipValidationError,
    2202: PartnershipValidationTimeout,
    2203: PartnershipAccessFailure,
    2204: PartnershipAccountInvalid,
    2205: PartnershipGetAccountInfoFailure,
    2206: PartnershipDisabled,
    2207: PartnershipAlreadyExists,
    2300: CommunityStreamingUnavailable,
    2500: TwitchNotLinked,
    2501: TwitchAccountNotFound,
    2502: TwitchCouldNotLoadDestinyInfo,
    2503: TwitchCouldNotRegisterUser,
    2504: TwitchCouldNotUnregisterUser,
    2505: TwitchRequiresRelinking,
    2506: TwitchNoPlatformChosen,
    2600: TrendingCategoryNotFound,
    2601: TrendingEntryTypeNotSupported,
    2700: ReportOffenderNotInPgcr,
    2701: ReportRequestorNotInPgcr,
    2702: ReportSubmissionFailed,
    2703: ReportCannotReportSelf,
    2800: AwaTypeDisabled,
    2801: AwaTooManyPendingRequests,
    2802: AwaTheFeatureRequiresARegisteredDevice,
    2803: AwaRequestWasUnansweredForTooLong,
    2804: AwaWriteRequestMissingOrInvalidToken,
    2805: AwaWriteRequestTokenExpired,
    2806: AwaWriteRequestTokenUsageLimitReached,
    2900: SteamWebApiError,
    2901: SteamWebNullResponseError,
    2902: SteamAccountRequired,
    2903: SteamNotAuthorized,
    3000: ClanFireteamNotFound,
    3001: ClanFireteamAddNoAlternatesForImmediate,
    3002: ClanFireteamFull,
    3003: ClanFireteamAltFull,
    3004: ClanFireteamBlocked,
    3005: ClanFireteamPlayerEntryNotFound,
    3006: ClanFireteamPermissions,
    3007: ClanFireteamInvalidPlatform,
    3008: ClanFireteamCannotAdjustSlotCount,
    3009: ClanFireteamInvalidPlayerPlatform,
    3010: ClanFireteamNotReadyForInvitesNotEnoughPlayers,
    3011: ClanFireteamGameInvitesNotSupportForPlatform,
    3012: ClanFireteamPlatformInvitePreqFailure,
    3013: ClanFireteamInvalidAuthContext,
    3014: ClanFireteamInvalidAuthProviderPsn,
    3015: ClanFireteamPs4SessionFull,
    3016: ClanFireteamInvalidAuthToken,
    3017: ClanFireteamScheduledFireteamsDisabled,
    3018: ClanFireteamNotReadyForInvitesNotScheduledYet,
    3019: ClanFireteamNotReadyForInvitesClosed,
    3020: ClanFireteamScheduledFireteamsRequireAdminPermissions,
    3021: ClanFireteamNonPublicMustHaveClan,
    3022: ClanFireteamPublicCreationRestriction,
    3023: ClanFireteamAlreadyJoined,
    3024: ClanFireteamScheduledFireteamsRange,
    3025: ClanFireteamPublicCreationRestrictionExtended,
    3026: ClanFireteamExpired,
    3027: ClanFireteamInvalidAuthProvider,
    3028: ClanFireteamInvalidAuthProviderXuid,
    3029: ClanFireteamThrottle,
    3030: ClanFireteamTooManyOpenScheduledFireteams,
    3031: ClanFireteamCannotReopenScheduledFireteams,
    3032: ClanFireteamJoinNoAccountSpecified,
    3033: ClanFireteamMinDestiny2ProgressForCreation,
    3034: ClanFireteamMinDestiny2ProgressForJoin,
    3035: ClanFireteamSMSOrPurchaseRequiredCreate,
    3036: ClanFireteamPurchaseRequiredCreate,
    3037: ClanFireteamSMSOrPurchaseRequiredJoin,
    3038: ClanFireteamPurchaseRequiredJoin,
    3200: CrossSaveOverriddenAccountNotFound,
    3201: CrossSaveTooManyOverriddenPlatforms,
    3202: CrossSaveNoOverriddenPlatforms,
    3203: CrossSavePrimaryAccountNotFound,
    3204: CrossSaveRequestInvalid,
    3206: CrossSaveBungieAccountValidationFailure,
    3207: CrossSaveOverriddenPlatformNotAllowed,
    3208: CrossSaveThresholdExceeded,
    3209: CrossSaveIncompatibleMembershipType,
    3210: CrossSaveCouldNotFindLinkedAccountForMembershipType,
    3211: CrossSaveCouldNotCreateDestinyProfileForMembershipType,
    3212: CrossSaveErrorCreatingDestinyProfileForMembershipType,
    3213: CrossSaveCannotOverrideSelf,
    3214: CrossSaveRecentSilverPurchase,
    3215: CrossSaveSilverBalanceNegative,
    3216: CrossSaveAccountNotAuthenticated,
    3217: ErrorOneAccountAlreadyActive,
    3218: ErrorOneAccountDestinyRestriction,
    3219: CrossSaveMustMigrateToSteam,
    3220: CrossSaveSteamAlreadyPaired,
    3221: CrossSaveCannotPairJustSteamAndBlizzard,
    3222: CrossSaveCannotPairSteamAloneBeforeShadowkeep,
    3300: AuthVerificationNotLinkedToAccount,
    3400: PCMigrationMissingBlizzard,
    3401: PCMigrationMissingSteam,
    3402: PCMigrationInvalidBlizzard,
    3403: PCMigrationInvalidSteam,
    3404: PCMigrationUnknownFailure,
    3405: PCMigrationUnknownException,
    3406: PCMigrationNotLinked,
    3407: PCMigrationAccountsAlreadyUsed,
    3408: PCMigrationStepFailed,
    3409: PCMigrationInvalidBlizzardCrossSaveState,
    3410: PCMigrationDestinationBanned,
    3411: PCMigrationDestinyFailure,
    3412: PCMigrationSilverTransferFailed,
    3413: PCMigrationEntitlementTransferFailed,
    3414: PCMigrationCannotStompClanFounder,
    3500: UnsupportedBrowser,
    3600: StadiaAccountRequired,
    3702: ErrorPhoneValidationTooManyUses,
    3703: ErrorPhoneValidationNoAssociatedPhone,
    3705: ErrorPhoneValidationCodeInvalid,
    3706: ErrorPhoneValidationBanned,
    3707: ErrorPhoneValidationCodeTooRecentlySent,
    3708: ErrorPhoneValidationCodeExpired,
    3709: ErrorPhoneValidationInvalidNumberType,
    3710: ErrorPhoneValidationCodeTooRecentlyChecked,
    3800: ApplePushErrorUnknown,
    3801: ApplePushErrorNull,
    3802: ApplePushErrorTimeout,
    3803: ApplePushBadRequest,
    3804: ApplePushFailedAuth,
    3805: ApplePushThrottled,
    3806: ApplePushServiceUnavailable,
    3807: NotAnImageOrVideo,
    3900: ErrorBungieFriendsBlockFailed,
    3901: ErrorBungieFriendsAutoReject,
    3902: ErrorBungieFriendsNoRequestFound,
    3903: ErrorBungieFriendsAlreadyFriends,
    3904: ErrorBungieFriendsUnableToRemoveRequest,
    3905: ErrorBungieFriendsUnableToRemove,
    3906: ErrorBungieFriendsIdenticalSourceTarget,
    3907: ErrorBungieFriendsSelf,
    3908: ErrorBungieBlockSelf,
    3910: ErrorBungieFriendsListFull,
    3911: ErrorBungieBlockListFull,
}
