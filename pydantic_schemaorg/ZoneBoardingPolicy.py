from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BoardingPolicyType import BoardingPolicyType


class ZoneBoardingPolicy(BoardingPolicyType):
    """The airline boards by zones of the plane.

    See: https://schema.org/ZoneBoardingPolicy
    Model depth: 5
    """

    type_: str = Field("ZoneBoardingPolicy", const=True, alias="@type")


if TYPE_CHECKING:

    ZoneBoardingPolicy.update_forward_refs()
