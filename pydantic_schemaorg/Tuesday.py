from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Tuesday(DayOfWeek):
    """The day of the week between Monday and Wednesday.

    See: https://schema.org/Tuesday
    Model depth: 5
    """
    type_: str = Field("Tuesday", alias='@type')
    

