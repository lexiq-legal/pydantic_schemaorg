from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class NonprofitType(Enumeration):
    """NonprofitType enumerates several kinds of official non-profit types of which a non-profit"
     "organization can be.

    See: https://schema.org/NonprofitType
    Model depth: 4
    """
    type_: str = Field("NonprofitType", alias='@type')
    

