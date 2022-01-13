from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class BoardingPolicyType(Enumeration):
    """A type of boarding policy used by an airline.

    See: https://schema.org/BoardingPolicyType
    Model depth: 4
    """

    type_: str = Field("BoardingPolicyType", const=True, alias="@type")


if TYPE_CHECKING:

    BoardingPolicyType.update_forward_refs()
