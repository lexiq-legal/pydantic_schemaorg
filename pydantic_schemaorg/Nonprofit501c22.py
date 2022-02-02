from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c22(USNonprofitType):
    """Nonprofit501c22: Non-profit type referring to Withdrawal Liability Payment Funds.

    See: https://schema.org/Nonprofit501c22
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c22", alias='@type')
    

