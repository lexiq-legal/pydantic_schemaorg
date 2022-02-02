from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Crematorium(CivicStructure):
    """A crematorium.

    See: https://schema.org/Crematorium
    Model depth: 4
    """
    type_: str = Field("Crematorium", alias='@type')
    

