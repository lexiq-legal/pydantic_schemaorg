from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BodyOfWater import BodyOfWater


class SeaBodyOfWater(BodyOfWater):
    """A sea (for example, the Caspian sea).

    See: https://schema.org/SeaBodyOfWater
    Model depth: 5
    """

    type_: str = Field("SeaBodyOfWater", const=True, alias="@type")


if TYPE_CHECKING:

    SeaBodyOfWater.update_forward_refs()
