from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Clip import Clip


class VideoGameClip(Clip):
    """A short segment/part of a video game.

    See: https://schema.org/VideoGameClip
    Model depth: 4
    """

    type_: str = Field("VideoGameClip", const=True, alias="@type")


if TYPE_CHECKING:

    VideoGameClip.update_forward_refs()
