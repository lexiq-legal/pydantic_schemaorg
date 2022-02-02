from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class HealthAndBeautyBusiness(LocalBusiness):
    """Health and beauty.

    See: https://schema.org/HealthAndBeautyBusiness
    Model depth: 4
    """
    type_: str = Field("HealthAndBeautyBusiness", alias='@type')
    

