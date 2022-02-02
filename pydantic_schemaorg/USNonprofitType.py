from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.NonprofitType import NonprofitType


class USNonprofitType(NonprofitType):
    """USNonprofitType: Non-profit organization type originating from the United States.

    See: https://schema.org/USNonprofitType
    Model depth: 5
    """
    type_: str = Field("USNonprofitType", alias='@type')
    

