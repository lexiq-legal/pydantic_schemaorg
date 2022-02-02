from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class GovernmentBuilding(CivicStructure):
    """A government building.

    See: https://schema.org/GovernmentBuilding
    Model depth: 4
    """
    type_: str = Field("GovernmentBuilding", alias='@type')
    

