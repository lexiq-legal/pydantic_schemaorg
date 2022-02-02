from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DayOfWeek import DayOfWeek


class Friday(DayOfWeek):
    """The day of the week between Thursday and Saturday.

    See: https://schema.org/Friday
    Model depth: 5
    """
    type_: str = Field("Friday", alias='@type')
    

