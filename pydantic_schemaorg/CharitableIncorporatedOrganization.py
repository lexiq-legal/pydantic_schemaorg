from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.UKNonprofitType import UKNonprofitType


class CharitableIncorporatedOrganization(UKNonprofitType):
    """CharitableIncorporatedOrganization: Non-profit type referring to a Charitable"
     "Incorporated Organization (UK).

    See: https://schema.org/CharitableIncorporatedOrganization
    Model depth: 6
    """
    type_: str = Field("CharitableIncorporatedOrganization", alias='@type')
    

