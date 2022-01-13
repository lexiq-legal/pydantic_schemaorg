from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class DemoAlbum(MusicAlbumProductionType):
    """DemoAlbum.

    See: https://schema.org/DemoAlbum
    Model depth: 5
    """

    type_: str = Field("DemoAlbum", const=True, alias="@type")


if TYPE_CHECKING:

    DemoAlbum.update_forward_refs()
