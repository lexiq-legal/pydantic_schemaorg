from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Bridge(CivicStructure):
    """A bridge.

    See: https://schema.org/Bridge
    Model depth: 4
    """
    type_: str = Field("Bridge", alias='@type')
    

