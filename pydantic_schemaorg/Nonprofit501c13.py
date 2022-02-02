from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c13(USNonprofitType):
    """Nonprofit501c13: Non-profit type referring to Cemetery Companies.

    See: https://schema.org/Nonprofit501c13
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c13", alias='@type')
    

