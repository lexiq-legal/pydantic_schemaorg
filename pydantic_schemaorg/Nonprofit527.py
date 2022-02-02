from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit527(USNonprofitType):
    """Nonprofit527: Non-profit type referring to Political organizations.

    See: https://schema.org/Nonprofit527
    Model depth: 6
    """
    type_: str = Field("Nonprofit527", alias='@type')
    

