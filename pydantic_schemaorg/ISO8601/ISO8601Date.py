import re
from typing import no_type_check, Optional, Dict, cast, Any, Pattern, TYPE_CHECKING, Generator, AnyStr, Union

from pydantic import BaseConfig
from pydantic.fields import ModelField
from pydantic.utils import update_not_none
from pydantic.validators import str_validator, constr_length_validator

from ISO8601 import errors

if TYPE_CHECKING:
    from pydantic.typing import AnyCallable

    CallableGenerator = Generator[AnyCallable, None, None]

_url_regex_cache: Union[Pattern[AnyStr], None] = None


def ISO8601Date_regex() -> Pattern[str]:
    global _url_regex_cache
    if _url_regex_cache is None:
        _url_regex_cache = re.compile(
            r'(?P<year>-?(?:[1-9][0-9]*)?[0-9]{4})-?(?P<month>1[0-2]|0[1-9])?-?(?P<day>3[01]|0[1-9]|[12][0-9])?(T(?P<hour>(2[0-3]|[01][0-9])))?(\:(?P<minute>[0-5][0-9]))?(\:(?P<second>[0-5][0-9]))?(\.(?P<microsecond>[0-9]+))?([+-](?P<timezone>([0-9]{2}\:[0-9]{2})|Z))?',
            re.IGNORECASE
        )
        return _url_regex_cache
    else:
        return _url_regex_cache


class ISO8601Date(str):
    strip_whitespace = True
    min_length = 1
    max_length = 2 ** 16

    __slots__ = ('date', 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond', 'tz')

    @no_type_check
    def __new__(cls, date: Optional[str], **kwargs) -> object:
        return str.__new__(cls, cls.build(**kwargs) if date is None else date)

    def __init__(
            self,
            date: str,
            *,
            year: Optional[int] = None,
            month: Optional[int] = None,
            day: Optional[int] = None,
            hour: Optional[int] = None,
            minute: Optional[int] = None,
            second: Optional[int] = None,
            microsecond: Optional[int] = None,
            tz: Optional[str] = None,
    ) -> None:
        str.__init__(date)
        self.date = date
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        self.tz = tz

    @classmethod
    def build(
            cls,
            date: str,
            *,
            year: int,
            month: Optional[int] = None,
            day: Optional[int] = None,
            hour: Optional[int] = None,
            minute: Optional[int] = None,
            second: Optional[int] = None,
            microsecond: Optional[int] = None,
            tz: Optional[str] = None,
    ) -> str:
        date = ''
        # TODO: put this in while loop
        if year:
            date += str(year)
            if month:
                date += '-' + str(month)
                if day:
                    date += '-' + str(month)
                    if hour:
                        date += 'T' + str(hour)
                        if minute:
                            date += ':' + str(minute)
                            if second:
                                date += ':' + str(second)
                                if microsecond:
                                    date += '.' + str(microsecond)
        return date

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        update_not_none(field_schema, minLength=cls.min_length, maxLength=cls.max_length, format='ISO8601')

    @classmethod
    def __get_validators__(cls) -> 'CallableGenerator':
        yield cls.validate

    def validate_iso_date(self, value: Any):
        value = str_validator(value)
        if self.__class__.strip_whitespace:
            value = value.strip()
        m = ISO8601Date_regex().match(value)
        assert m, 'ISO8601Date regex failed unexpectedly'

        parts = m.groupdict()
        parts = self.__class__.validate_parts(parts)

    @classmethod
    def validate(cls, value: Any, field: 'ModelField', config: 'BaseConfig') -> 'ISO8601Date':
        if value.__class__ == cls:
            return value
        value = str_validator(value)
        if cls.strip_whitespace:
            value = value.strip()
        date: str = cast(str, constr_length_validator(value, field, config))

        m = ISO8601Date_regex().match(date)
        assert m, 'ISO8601Date regex failed unexpectedly'

        parts = m.groupdict()
        parts = cls.validate_parts(parts)

        if m.end() != len(date):
            raise ValueError()

        return cls(
            date,
            year=parts['year'],
            month=parts['month'],
            day=parts['day'],
            hour=parts['hour'],
            minute=parts['minute'],
            second=parts['second'],
            microsecond=parts['microsecond'],
            tz=parts['tz'],
        )

    @classmethod
    def validate_parts(cls, parts: Dict[str, str]) -> Dict[str, Union[str, int]]:
        """
        A method used to validate parts of an ISO8601.
        """
        parts_order = ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond', 'tz']
        year = parts['year']
        if year is None:
            raise errors.ISO8601DateInvalid()

        for part_order in parts_order:
            parts[part_order] = parts.get(part_order, None)
            if parts[part_order] is not None and part_order != 'tz':
                parts[part_order] = int(parts[part_order])

        return parts
