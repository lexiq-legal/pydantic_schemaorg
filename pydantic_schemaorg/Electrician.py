from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class Electrician(HomeAndConstructionBusiness):
    """An electrician.

    See: https://schema.org/Electrician
    Model depth: 5
    """
    type_: str = Field("Electrician", alias='@type')
    

