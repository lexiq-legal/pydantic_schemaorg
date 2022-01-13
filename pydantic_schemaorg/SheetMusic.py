from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CreativeWork import CreativeWork


class SheetMusic(CreativeWork):
    """Printed music, as opposed to performed or recorded music.

    See: https://schema.org/SheetMusic
    Model depth: 3
    """

    type_: str = Field("SheetMusic", const=True, alias="@type")


if TYPE_CHECKING:

    SheetMusic.update_forward_refs()
