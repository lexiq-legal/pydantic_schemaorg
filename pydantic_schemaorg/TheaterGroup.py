from pydantic import Field
from pydantic_schemaorg.PerformingGroup import PerformingGroup


class TheaterGroup(PerformingGroup):
    """A theater group or company, for example, the Royal Shakespeare Company or Druid Theatre.

    See https://schema.org/TheaterGroup.

    """
    type_: str = Field("TheaterGroup", const=True, alias='@type')
    

TheaterGroup.update_forward_refs()
