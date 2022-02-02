from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c12(USNonprofitType):
    """Nonprofit501c12: Non-profit type referring to Benevolent Life Insurance Associations,"
     "Mutual Ditch or Irrigation Companies, Mutual or Cooperative Telephone Companies.

    See: https://schema.org/Nonprofit501c12
    Model depth: 6
    """
    type_: str = Field("Nonprofit501c12", alias='@type')
    

