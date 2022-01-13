from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BodyOfWater import BodyOfWater


class OceanBodyOfWater(BodyOfWater):
    """An ocean (for example, the Pacific).

    See: https://schema.org/OceanBodyOfWater
    Model depth: 5
    """

    type_: str = Field("OceanBodyOfWater", const=True, alias="@type")


if TYPE_CHECKING:

    OceanBodyOfWater.update_forward_refs()
