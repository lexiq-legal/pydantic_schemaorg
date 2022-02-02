from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class MovingCompany(HomeAndConstructionBusiness):
    """A moving company.

    See: https://schema.org/MovingCompany
    Model depth: 5
    """
    type_: str = Field("MovingCompany", alias='@type')
    

