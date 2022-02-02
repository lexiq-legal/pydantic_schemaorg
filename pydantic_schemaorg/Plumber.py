from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class Plumber(HomeAndConstructionBusiness):
    """A plumbing service.

    See: https://schema.org/Plumber
    Model depth: 5
    """
    type_: str = Field("Plumber", alias='@type')
    

