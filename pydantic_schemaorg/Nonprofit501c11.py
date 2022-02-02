from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c11(USNonprofitType):
    """Nonprofit501c11: Non-profit type referring to Teachers' Retirement Fund Associations.

    See: https://schema.org/Nonprofit501c11
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c11", alias='@type')
    

