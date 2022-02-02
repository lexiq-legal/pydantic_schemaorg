from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c16(USNonprofitType):
    """Nonprofit501c16: Non-profit type referring to Cooperative Organizations to Finance"
     "Crop Operations.

    See: https://schema.org/Nonprofit501c16
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c16", alias='@type')
    

