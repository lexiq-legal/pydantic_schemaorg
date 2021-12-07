from pydantic import Field
from pydantic_schemaorg.PerformingGroup import PerformingGroup


class DanceGroup(PerformingGroup):
    """A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.

    See https://schema.org/DanceGroup.

    """
    type_: str = Field("DanceGroup", const=True, alias='@type')
    

DanceGroup.update_forward_refs()
