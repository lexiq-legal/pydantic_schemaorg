from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Sunday(DayOfWeek):
    """The day of the week between Saturday and Monday.

    See: https://schema.org/Sunday
    Model depth: 5
    """
    type_: str = Field("Sunday", alias='@type')
    

