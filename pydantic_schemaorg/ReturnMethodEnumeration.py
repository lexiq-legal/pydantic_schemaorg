from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class ReturnMethodEnumeration(Enumeration):
    """Enumerates several types of product return methods.

    See: https://schema.org/ReturnMethodEnumeration
    Model depth: 4
    """

    type_: str = Field("ReturnMethodEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    ReturnMethodEnumeration.update_forward_refs()
