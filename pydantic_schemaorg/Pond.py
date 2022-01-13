from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BodyOfWater import BodyOfWater


class Pond(BodyOfWater):
    """A pond.

    See: https://schema.org/Pond
    Model depth: 5
    """

    type_: str = Field("Pond", const=True, alias="@type")


if TYPE_CHECKING:

    Pond.update_forward_refs()
