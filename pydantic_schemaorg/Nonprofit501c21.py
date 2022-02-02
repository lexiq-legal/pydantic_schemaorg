from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c21(USNonprofitType):
    """Nonprofit501c21: Non-profit type referring to Black Lung Benefit Trusts.

    See: https://schema.org/Nonprofit501c21
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c21", alias='@type')
    

