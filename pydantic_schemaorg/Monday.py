from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Monday(DayOfWeek):
    """The day of the week between Sunday and Tuesday.

    See: https://schema.org/Monday
    Model depth: 5
    """
    type_: str = Field("Monday", alias='@type')
    

