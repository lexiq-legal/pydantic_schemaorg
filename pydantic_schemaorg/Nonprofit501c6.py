from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c6(USNonprofitType):
    """Nonprofit501c6: Non-profit type referring to Business Leagues, Chambers of Commerce,"
     "Real Estate Boards.

    See: https://schema.org/Nonprofit501c6
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c6", alias='@type')
    

