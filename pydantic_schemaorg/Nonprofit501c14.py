from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c14(USNonprofitType):
    """Nonprofit501c14: Non-profit type referring to State-Chartered Credit Unions, Mutual"
     "Reserve Funds.

    See: https://schema.org/Nonprofit501c14
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c14", alias='@type')
    

