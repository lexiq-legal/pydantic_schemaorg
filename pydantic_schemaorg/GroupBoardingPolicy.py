from pydantic import Field
from pydantic_schemaorg.BoardingPolicyType import BoardingPolicyType


class GroupBoardingPolicy(BoardingPolicyType):
    """The airline boards by groups based on check-in time, priority, etc.

    See https://schema.org/GroupBoardingPolicy.

    """
    type_: str = Field("GroupBoardingPolicy", const=True, alias='@type')
    

GroupBoardingPolicy.update_forward_refs()
