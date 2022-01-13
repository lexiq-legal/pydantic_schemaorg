from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class HinduTemple(PlaceOfWorship):
    """A Hindu temple.

    See: https://schema.org/HinduTemple
    Model depth: 5
    """

    type_: str = Field("HinduTemple", const=True, alias="@type")


if TYPE_CHECKING:

    HinduTemple.update_forward_refs()
