from arya_api_framework import BaseModel


__all__ = [
    'UserTheme',
    'GroupTheme'
]


class UserTheme(BaseModel):
    userThemeId: int
    userThemeName: str
    userThemeDescription: str


class GroupTheme(BaseModel):
    name: str
    folder: str
    description: str
