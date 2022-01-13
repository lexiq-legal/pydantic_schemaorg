from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class SizeGroupEnumeration(Enumeration):
    """Enumerates common size groups for various product categories.

    See: https://schema.org/SizeGroupEnumeration
    Model depth: 4
    """

    type_: str = Field("SizeGroupEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    SizeGroupEnumeration.update_forward_refs()
