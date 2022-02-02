from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.UKNonprofitType import UKNonprofitType


class UKTrust(UKNonprofitType):
    """UKTrust: Non-profit type referring to a UK trust.

    See: https://schema.org/UKTrust
    Model depth: 6
    """
    type_: str = Field("UKTrust", alias='@type')
    

