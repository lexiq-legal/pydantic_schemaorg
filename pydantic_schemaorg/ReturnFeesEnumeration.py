from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class ReturnFeesEnumeration(Enumeration):
    """Enumerates several kinds of policies for product return fees.

    See: https://schema.org/ReturnFeesEnumeration
    Model depth: 4
    """

    type_: str = Field("ReturnFeesEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    ReturnFeesEnumeration.update_forward_refs()
