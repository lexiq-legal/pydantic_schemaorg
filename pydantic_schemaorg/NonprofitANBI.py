from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.NLNonprofitType import NLNonprofitType


class NonprofitANBI(NLNonprofitType):
    """NonprofitANBI: Non-profit type referring to a Public Benefit Organization (NL).

    See: https://schema.org/NonprofitANBI
    Model depth: 6
    """
    type_: str = Field("NonprofitANBI", alias='@type')
    

