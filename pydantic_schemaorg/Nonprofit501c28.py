from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c28(USNonprofitType):
    """Nonprofit501c28: Non-profit type referring to National Railroad Retirement Investment"
     "Trusts.

    See: https://schema.org/Nonprofit501c28
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c28", alias='@type')
    

