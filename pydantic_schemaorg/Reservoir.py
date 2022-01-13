from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BodyOfWater import BodyOfWater


class Reservoir(BodyOfWater):
    """A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.

    See: https://schema.org/Reservoir
    Model depth: 5
    """

    type_: str = Field("Reservoir", const=True, alias="@type")


if TYPE_CHECKING:

    Reservoir.update_forward_refs()
