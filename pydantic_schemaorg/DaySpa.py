from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class DaySpa(HealthAndBeautyBusiness):
    """A day spa.

    See: https://schema.org/DaySpa
    Model depth: 5
    """
    type_: str = Field("DaySpa", alias='@type')
    

