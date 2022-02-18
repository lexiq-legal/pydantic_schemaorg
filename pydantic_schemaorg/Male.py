from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GenderType import GenderType


class Male(GenderType):
    """The male gender.

    See: https://schema.org/Male
    Model depth: 5
    """
    type_: str = Field(default="Male", alias='@type', const=True)
    
