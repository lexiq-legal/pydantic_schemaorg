from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CreativeWork import CreativeWork


class Season(CreativeWork):
    """A media season e.g. tv, radio, video game etc.

    See: https://schema.org/Season
    Model depth: 3
    """

    type_: str = Field("Season", const=True, alias="@type")


if TYPE_CHECKING:

    Season.update_forward_refs()
