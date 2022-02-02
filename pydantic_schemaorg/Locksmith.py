from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class Locksmith(HomeAndConstructionBusiness):
    """A locksmith.

    See: https://schema.org/Locksmith
    Model depth: 5
    """
    type_: str = Field("Locksmith", alias='@type')
    

