from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Zoo(CivicStructure):
    """A zoo.

    See: https://schema.org/Zoo
    Model depth: 4
    """
    type_: str = Field("Zoo", alias='@type')
    

