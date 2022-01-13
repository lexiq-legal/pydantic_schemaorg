from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class GenderType(Enumeration):
    """An enumeration of genders.

    See: https://schema.org/GenderType
    Model depth: 4
    """

    type_: str = Field("GenderType", const=True, alias="@type")


if TYPE_CHECKING:

    GenderType.update_forward_refs()
