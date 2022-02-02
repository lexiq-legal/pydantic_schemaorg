from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501n(USNonprofitType):
    """Nonprofit501n: Non-profit type referring to Charitable Risk Pools.

    See: https://schema.org/Nonprofit501n
    Model depth: 6
    """
    type_: str = Field("Nonprofit501n", alias='@type')
    

