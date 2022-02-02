from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class BeautySalon(HealthAndBeautyBusiness):
    """Beauty salon.

    See: https://schema.org/BeautySalon
    Model depth: 5
    """
    type_: str = Field("BeautySalon", alias='@type')
    

