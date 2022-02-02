from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c25(USNonprofitType):
    """Nonprofit501c25: Non-profit type referring to Real Property Title-Holding Corporations"
     "or Trusts with Multiple Parents.

    See: https://schema.org/Nonprofit501c25
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c25", alias='@type')
    

