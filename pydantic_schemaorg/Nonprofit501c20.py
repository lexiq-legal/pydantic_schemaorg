from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c20(USNonprofitType):
    """Nonprofit501c20: Non-profit type referring to Group Legal Services Plan Organizations.

    See: https://schema.org/Nonprofit501c20
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c20", alias='@type')
    

