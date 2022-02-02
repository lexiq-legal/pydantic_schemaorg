from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c27(USNonprofitType):
    """Nonprofit501c27: Non-profit type referring to State-Sponsored Workers' Compensation"
     "Reinsurance Organizations.

    See: https://schema.org/Nonprofit501c27
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c27", alias='@type')
    

