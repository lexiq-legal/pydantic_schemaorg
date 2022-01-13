from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class Synagogue(PlaceOfWorship):
    """A synagogue.

    See: https://schema.org/Synagogue
    Model depth: 5
    """

    type_: str = Field("Synagogue", const=True, alias="@type")


if TYPE_CHECKING:

    Synagogue.update_forward_refs()
