from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Aquarium(CivicStructure):
    """Aquarium.

    See: https://schema.org/Aquarium
    Model depth: 4
    """
    type_: str = Field("Aquarium", alias='@type')
    

