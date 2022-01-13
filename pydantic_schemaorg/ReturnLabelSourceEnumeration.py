from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class ReturnLabelSourceEnumeration(Enumeration):
    """Enumerates several types of return labels for product returns.

    See: https://schema.org/ReturnLabelSourceEnumeration
    Model depth: 4
    """

    type_: str = Field("ReturnLabelSourceEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    ReturnLabelSourceEnumeration.update_forward_refs()
