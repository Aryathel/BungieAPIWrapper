from enum import IntEnum, IntFlag, Enum
from typing import Any, List, Generator, Union, Iterable, Optional

from pydantic.fields import ModelField


__all__ = [
    'DocumentedIntEnum',
    'DocumentedIntFlag',
]


IntEnumT = Union[str, int, 'DocumentedIntEnum']


# ==================
#      Classes
# ==================
class EnumValidatorType(Enum):
    Default = None
    String = 'str'
    Int = 'int'
    StringList = 'str_list'
    IntList = 'int_list'
    IntListString = 'int_list_str'
    StringListString = 'str_list_str'


class DocumentedIntEnum(IntEnum):
    def __new__(cls, value: int, doc: str = None) -> IntEnum:
        self = int.__new__(cls, value)
        self._value_ = value
        if doc is not None:
            self.__doc__ = doc
        return self

    @classmethod
    def __get_validators__(cls):
        yield cls.validator

    @classmethod
    def validator(cls, o: Union[IntEnumT, List[IntEnumT]], field: ModelField) -> Any:
        v_type = EnumValidatorType(field.field_info.extra.get('type'))

        if v_type == EnumValidatorType.Default:
            return cls.default_validator(o)
        elif v_type == EnumValidatorType.String:
            return cls.str_validator(o)
        elif v_type == EnumValidatorType.Int:
            return cls.int_validator(o)
        elif v_type == EnumValidatorType.StringList:
            return cls.str_list_validator(o)
        elif v_type == EnumValidatorType.IntList:
            return cls.int_list_validator(o)
        elif v_type == EnumValidatorType.StringListString:
            return cls.str_list_str_validator(o)
        elif v_type == EnumValidatorType.IntListString:
            return cls.int_list_str_validator(o)

    @classmethod
    def default_validator(cls, o: IntEnumT):
        if hasattr(cls, str(o)):
            return getattr(cls, str(o))
        try:
            o = int(o)
        except ValueError:
            pass
        return cls(o)

    @classmethod
    def int_validator(cls, o: IntEnumT) -> int:
        return int(cls.default_validator(o))

    @classmethod
    def str_validator(cls, o: IntEnumT) -> str:
        return str(cls.default_validator(o))

    @classmethod
    def list_validator(cls, o: Union[IntEnumT, List[IntEnumT]]) -> List['DocumentedIntEnum']:
        if not isinstance(o, Iterable):
            o = [o]

        vals = []
        for comp in o:
            vals.append(cls.default_validator(comp))
        return vals

    @classmethod
    def int_list_validator(cls, o: Union[IntEnumT, List[IntEnumT]]) -> List[int]:
        return [int(v) for v in cls.list_validator(o)]

    @classmethod
    def str_list_validator(cls, o: Union[IntEnumT, List[IntEnumT]]) -> List[str]:
        return [str(v.name) for v in cls.list_validator(o)]

    @classmethod
    def int_list_str_validator(cls, o: Union[IntEnumT, List[IntEnumT]]) -> str:
        return ','.join(str(v) for v in cls.int_list_validator(o))

    @classmethod
    def str_list_str_validator(cls, o: Union[IntEnumT, List[IntEnumT]]) -> str:
        return ','.join(cls.str_list_validator(o))


class DocumentedIntFlag(IntFlag):
    def __new__(cls, value: int, doc: str = None) -> IntFlag:
        self = int.__new__(cls, value)
        self._value_ = value
        if doc is not None:
            self.__doc__ = doc
        return self

    @classmethod
    def members(cls, flag: IntFlag) -> List[IntFlag]:
        return [f for f in cls if f in flag]

    @classmethod
    def __get_validators__(cls):
        yield cls.validator

    @classmethod
    def validator(cls, o: Union[IntEnumT, List[IntEnumT]], field: ModelField) -> Any:
        v_type = EnumValidatorType(field.field_info.extra.get('type'))

        if v_type == EnumValidatorType.Default:
            return cls.default_validator(o)

    @classmethod
    def default_validator(cls, o: IntEnumT):
        if hasattr(cls, str(o)):
            return getattr(cls, str(o))
        return cls(int(o))
