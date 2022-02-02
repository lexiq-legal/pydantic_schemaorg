from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501a(USNonprofitType):
    """Nonprofit501a: Non-profit type referring to Farmers’ Cooperative Associations.

    See: https://schema.org/Nonprofit501a
    Model depth: 6
    """
    type_: str = Field("Nonprofit501a", alias='@type')
    

