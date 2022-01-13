from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BodyOfWater import BodyOfWater


class RiverBodyOfWater(BodyOfWater):
    """A river (for example, the broad majestic Shannon).

    See: https://schema.org/RiverBodyOfWater
    Model depth: 5
    """

    type_: str = Field("RiverBodyOfWater", const=True, alias="@type")


if TYPE_CHECKING:

    RiverBodyOfWater.update_forward_refs()
