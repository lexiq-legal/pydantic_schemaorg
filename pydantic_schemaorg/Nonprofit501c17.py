from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c17(USNonprofitType):
    """Nonprofit501c17: Non-profit type referring to Supplemental Unemployment Benefit"
     "Trusts.

    See: https://schema.org/Nonprofit501c17
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c17", alias='@type')
    

