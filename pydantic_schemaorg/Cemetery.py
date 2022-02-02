from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Cemetery(CivicStructure):
    """A graveyard.

    See: https://schema.org/Cemetery
    Model depth: 4
    """
    type_: str = Field("Cemetery", alias='@type')
    

