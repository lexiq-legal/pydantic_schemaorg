from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BoardingPolicyType import BoardingPolicyType


class GroupBoardingPolicy(BoardingPolicyType):
    """The airline boards by groups based on check-in time, priority, etc.

    See: https://schema.org/GroupBoardingPolicy
    Model depth: 5
    """
    type_: str = Field("GroupBoardingPolicy", alias='@type')
    

