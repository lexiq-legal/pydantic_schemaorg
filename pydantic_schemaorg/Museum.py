from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Museum(CivicStructure):
    """A museum.

    See: https://schema.org/Museum
    Model depth: 4
    """
    type_: str = Field("Museum", alias='@type')
    

