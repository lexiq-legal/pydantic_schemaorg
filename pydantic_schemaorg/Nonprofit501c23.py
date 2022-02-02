from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c23(USNonprofitType):
    """Nonprofit501c23: Non-profit type referring to Veterans Organizations.

    See: https://schema.org/Nonprofit501c23
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c23", alias='@type')
    

