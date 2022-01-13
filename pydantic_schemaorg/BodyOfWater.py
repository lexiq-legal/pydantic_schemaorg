from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Landform import Landform


class BodyOfWater(Landform):
    """A body of water, such as a sea, ocean, or lake.

    See: https://schema.org/BodyOfWater
    Model depth: 4
    """

    type_: str = Field("BodyOfWater", const=True, alias="@type")


if TYPE_CHECKING:

    BodyOfWater.update_forward_refs()
