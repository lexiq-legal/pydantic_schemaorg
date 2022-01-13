from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BodyOfWater import BodyOfWater


class Waterfall(BodyOfWater):
    """A waterfall, like Niagara.

    See: https://schema.org/Waterfall
    Model depth: 5
    """

    type_: str = Field("Waterfall", const=True, alias="@type")


if TYPE_CHECKING:

    Waterfall.update_forward_refs()
