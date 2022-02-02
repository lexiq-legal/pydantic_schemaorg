from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class HousePainter(HomeAndConstructionBusiness):
    """A house painting service.

    See: https://schema.org/HousePainter
    Model depth: 5
    """
    type_: str = Field("HousePainter", alias='@type')
    

