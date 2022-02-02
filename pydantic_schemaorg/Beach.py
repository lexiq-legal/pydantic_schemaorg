from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Beach(CivicStructure):
    """Beach.

    See: https://schema.org/Beach
    Model depth: 4
    """
    type_: str = Field("Beach", alias='@type')
    

