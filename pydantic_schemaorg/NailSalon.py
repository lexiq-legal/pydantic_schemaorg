from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class NailSalon(HealthAndBeautyBusiness):
    """A nail salon.

    See: https://schema.org/NailSalon
    Model depth: 5
    """
    type_: str = Field("NailSalon", alias='@type')
    

