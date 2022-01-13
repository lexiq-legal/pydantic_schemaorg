from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class BuddhistTemple(PlaceOfWorship):
    """A Buddhist temple.

    See: https://schema.org/BuddhistTemple
    Model depth: 5
    """

    type_: str = Field("BuddhistTemple", const=True, alias="@type")


if TYPE_CHECKING:

    BuddhistTemple.update_forward_refs()
