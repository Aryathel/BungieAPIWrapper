from typing import (
    List,
    Mapping,
    Optional,
)

from arya_api_framework import BaseModel

from .enums import ContentPropertyDataTypeEnum


__all__ = [
    'ContentTypeDescription',
    'ContentTypeProperty',
    'ContentTypeDefaultValue',
    'TagMetadataDefinition',
    'TagMetadataItem',
    'ContentPreview',
    'ContentTypePropertySection',
]


class TagMetadataItem(BaseModel):
    description: str
    tagText: str
    groups: List[str]
    isDefault: bool
    name: str


class TagMetadataDefinition(BaseModel):
    description: str
    order: int
    items: List[TagMetadataItem]
    datatype: ContentPropertyDataTypeEnum
    name: str
    isRequired: bool


class ContentTypeDefaultValue(BaseModel):
    whenClause: str
    whenValue: str
    defaultValue: str


class ContentTypeProperty(BaseModel):
    name: str
    rootPropertyName: str
    readableName: str
    value: Optional[str]
    propertyDescription: str
    localizable: bool
    fallback: bool
    enabled: bool
    order: int
    visible: bool
    isTitle: bool
    required: bool
    maxLength: int
    maxByteLength: int
    maxFileSize: int
    regexp: str
    validateAs: str
    rssAttribute: str
    visibleDependency: str
    visibleOn: str
    datatype: ContentPropertyDataTypeEnum
    attributes: Mapping[str, str]
    childProperties: Optional[List['ContentTypeProperty']]
    contentTypeAllowed: str
    bindToProperty: str
    boundRegex: str
    representationSelection: Mapping[str, str]
    defaultValues: List[ContentTypeDefaultValue]
    isExternalAllowed: bool
    propertySection: Optional[str]
    weight: int
    entitytype: Optional[str]
    isCombo: bool
    suppressProperty: bool
    legalContentTypes: List[str]
    representationValidationString: str
    minWidth: Optional[int]
    maxWidth: Optional[int]
    minHeight: Optional[int]
    isVideo: Optional[bool]
    isImage: Optional[bool]


class ContentPreview(BaseModel):
    name: str
    path: str
    itemInSet: bool
    setTag: Optional[str]
    setNesting: int
    useSetId: int


class ContentTypePropertySection(BaseModel):
    name: str
    readableName: str
    collapsed: bool


class ContentTypeDescription(BaseModel):
    cType: str
    name: str
    contentDescription: str
    previewImage: str
    priority: int
    reminder: str
    properties: Optional[List[ContentTypeProperty]]
    tagMetadata: List[TagMetadataDefinition]
    tagMetadataItems: Mapping[str, TagMetadataItem]
    usageExamples: List[str]
    showInContentEditor: bool
    typeOf: str
    bindIdentifierToProperty: str
    boundRegex: str
    forceIdentifierBinding: bool
    allowComments: bool
    autoEnglishPropertyFallback: bool
    bulkUploadable: bool
    previews: List[ContentPreview]
    suppressCmsPath: bool
    propertySections: List[ContentTypePropertySection]
