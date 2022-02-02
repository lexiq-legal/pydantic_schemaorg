from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class GenderType(Enumeration):
    """An enumeration of genders.

    See: https://schema.org/GenderType
    Model depth: 4
    """
    type_: str = Field("GenderType", alias='@type')
    

