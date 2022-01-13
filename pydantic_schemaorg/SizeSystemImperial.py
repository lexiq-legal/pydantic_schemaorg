from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration


class SizeSystemImperial(SizeSystemEnumeration):
    """Imperial size system.

    See: https://schema.org/SizeSystemImperial
    Model depth: 5
    """

    type_: str = Field("SizeSystemImperial", const=True, alias="@type")


if TYPE_CHECKING:

    SizeSystemImperial.update_forward_refs()
