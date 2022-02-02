from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class LegislativeBuilding(GovernmentBuilding):
    """A legislative building&#x2014;for example, the state capitol.

    See: https://schema.org/LegislativeBuilding
    Model depth: 5
    """
    type_: str = Field("LegislativeBuilding", alias='@type')
    

