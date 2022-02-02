from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BoardingPolicyType import BoardingPolicyType


class ZoneBoardingPolicy(BoardingPolicyType):
    """The airline boards by zones of the plane.

    See: https://schema.org/ZoneBoardingPolicy
    Model depth: 5
    """
    type_: str = Field("ZoneBoardingPolicy", alias='@type')
    

