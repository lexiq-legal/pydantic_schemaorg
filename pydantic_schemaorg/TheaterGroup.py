from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PerformingGroup import PerformingGroup


class TheaterGroup(PerformingGroup):
    """A theater group or company, for example, the Royal Shakespeare Company or Druid Theatre.

    See: https://schema.org/TheaterGroup
    Model depth: 4
    """
    type_: str = Field("TheaterGroup", alias='@type')
    

