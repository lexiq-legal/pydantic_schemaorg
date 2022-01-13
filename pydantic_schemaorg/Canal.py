from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BodyOfWater import BodyOfWater


class Canal(BodyOfWater):
    """A canal, like the Panama Canal.

    See: https://schema.org/Canal
    Model depth: 5
    """

    type_: str = Field("Canal", const=True, alias="@type")


if TYPE_CHECKING:

    Canal.update_forward_refs()
