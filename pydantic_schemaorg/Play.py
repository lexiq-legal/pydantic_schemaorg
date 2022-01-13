from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CreativeWork import CreativeWork


class Play(CreativeWork):
    """A play is a form of literature, usually consisting of dialogue between characters, intended"
     "for theatrical performance rather than just reading. Note: A performance of a Play would"
     "be a [[TheaterEvent]] or [[BroadcastEvent]] - the *Play* being the [[workPerformed]].

    See: https://schema.org/Play
    Model depth: 3
    """

    type_: str = Field("Play", const=True, alias="@type")


if TYPE_CHECKING:

    Play.update_forward_refs()
