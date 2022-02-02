from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class TattooParlor(HealthAndBeautyBusiness):
    """A tattoo parlor.

    See: https://schema.org/TattooParlor
    Model depth: 5
    """
    type_: str = Field("TattooParlor", alias='@type')
    

