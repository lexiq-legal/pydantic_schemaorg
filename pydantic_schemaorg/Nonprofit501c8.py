from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c8(USNonprofitType):
    """Nonprofit501c8: Non-profit type referring to Fraternal Beneficiary Societies and"
     "Associations.

    See: https://schema.org/Nonprofit501c8
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c8", alias='@type')
    

