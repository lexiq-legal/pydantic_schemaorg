import re
from typing import no_type_check, Optional, Dict, cast, Any, Pattern

from pydantic import BaseConfig
from pydantic.fields import ModelField
from pydantic.typing import CallableGenerator
from pydantic.utils import update_not_none
from pydantic.validators import str_validator, constr_length_validator

from ISO8601 import errors


def ISO8601Date_regex() -> Pattern[str]:
    global _url_regex_cache
    if _url_regex_cache is None:
        _url_regex_cache = re.compile(
            r'^(?P<year>-?(?:[1-9][0-9]*)?[0-9]{4})-(?P<month>1[0-2]|0[1-9])(?P<day>3[01]|0[1-9]|[12][0-9])T(?P<hour>2[0-3]|[01][0-9])(?P<minute>[0-5][0-9]):(?P<second>[0-5][0-9])(?P<microsecond>\.[0-9]+)(?P<timezone>Z|[+-](?:2[0-3]|[01][0-9]):[0-5][0-9])?$',  # scheme https://tools.ietf.org/html/rfc3986#appendix-A
            re.IGNORECASE
        )
        return _url_regex_cache

    class ISO8601Date(str):
        strip_whitespace = True
        min_length = 1
        max_length = 2 ** 16

        __slots__ = ('year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond', 'tz')

        @no_type_check
        def __new__(cls, date: Optional[str], **kwargs) -> object:
            return str.__new__(cls, cls.build(**kwargs) if date is None else date)

        def __init__(
                self,
                date: str,
                *,
                year: int,
                month: Optional[int] = None,
                day: Optional[int] = None,
                hour: int,
                minute: Optional[int] = None,
                second: int = None,
                microsecond: int = None,
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

            host, tld, host_type, rebuild = cls.validate_host(parts)

            if m.end() != len(date):
                raise ValueError()

            return cls(
                None if rebuild else date,
                year=int(parts['year']),
                month=int(parts['month']),
                day=int(parts['day']),
                hour=int(parts['hour']),
                minute=int(parts['minute']),
                second=int(parts['second']),
                microsecond=int(parts['microsecond']),
                tz=parts['tz'],
            )

        @classmethod
        def validate_parts(cls, parts: Dict[str, str]) -> Dict[str, str]:
            """
            A method used to validate parts of an URL.
            Could be overridden to set default values for parts if missing
            """
            year = parts['year']
            if year is None:
                raise errors.ISO8601DateInvalid()

            return parts

        # @classmethod
        # def validate_host(cls, parts: Dict[str, str]) -> Tuple[str, Optional[str], str, bool]:
        #     host, tld, host_type, rebuild = None, None, None, False
        #     for f in ('domain', 'ipv4', 'ipv6'):
        #         host = parts[f]
        #         if host:
        #             host_type = f
        #             break
        #
        #     if host is None:
        #         raise errors.UrlHostError()
        #     elif host_type == 'domain':
        #         is_international = False
        #         d = ascii_domain_regex().fullmatch(host)
        #         if d is None:
        #             d = int_domain_regex().fullmatch(host)
        #             if d is None:
        #                 raise errors.UrlHostError()
        #             is_international = True
        #
        #         tld = d.group('tld')
        #         if tld is None and not is_international:
        #             d = int_domain_regex().fullmatch(host)
        #             tld = d.group('tld')
        #             is_international = True
        #
        #         if tld is not None:
        #             tld = tld[1:]
        #         elif cls.tld_required:
        #             raise errors.UrlHostTldError()
        #
        #         if is_international:
        #             host_type = 'int_domain'
        #             rebuild = True
        #             host = host.encode('idna').decode('ascii')
        #             if tld is not None:
        #                 tld = tld.encode('idna').decode('ascii')
        #
        #     return host, tld, host_type, rebuild  # type: ignore
