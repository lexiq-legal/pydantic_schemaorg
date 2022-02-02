from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Saturday(DayOfWeek):
    """The day of the week between Friday and Sunday.

    See: https://schema.org/Saturday
    Model depth: 5
    """
    type_: str = Field("Saturday", alias='@type')
    

