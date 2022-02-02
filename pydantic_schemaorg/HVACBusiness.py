from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class HVACBusiness(HomeAndConstructionBusiness):
    """A business that provide Heating, Ventilation and Air Conditioning services.

    See: https://schema.org/HVACBusiness
    Model depth: 5
    """
    type_: str = Field("HVACBusiness", alias='@type')
    

