from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c26(USNonprofitType):
    """Nonprofit501c26: Non-profit type referring to State-Sponsored Organizations Providing"
     "Health Coverage for High-Risk Individuals.

    See: https://schema.org/Nonprofit501c26
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c26", alias='@type')
    

