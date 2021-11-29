from pydantic import Field
from pydantic_schemaorg.BoardingPolicyType import BoardingPolicyType


class GroupBoardingPolicy(BoardingPolicyType):
    """The airline boards by groups based on check-in time, priority, etc.

    See https://schema.org/GroupBoardingPolicy.

    """

    locals().update({"@type": Field("GroupBoardingPolicy", const=True)})


GroupBoardingPolicy.update_forward_refs()
