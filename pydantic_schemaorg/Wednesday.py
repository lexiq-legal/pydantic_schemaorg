from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Wednesday(DayOfWeek):
    """The day of the week between Tuesday and Thursday.

    See: https://schema.org/Wednesday
    Model depth: 5
    """
    type_: str = Field("Wednesday", alias='@type')
    

