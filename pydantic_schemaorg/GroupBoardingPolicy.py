from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BoardingPolicyType import BoardingPolicyType


class GroupBoardingPolicy(BoardingPolicyType):
    """The airline boards by groups based on check-in time, priority, etc.

    See: https://schema.org/GroupBoardingPolicy
    Model depth: 5
    """

    type_: str = Field("GroupBoardingPolicy", const=True, alias="@type")


if TYPE_CHECKING:

    GroupBoardingPolicy.update_forward_refs()
