from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class CompilationAlbum(MusicAlbumProductionType):
    """CompilationAlbum.

    See: https://schema.org/CompilationAlbum
    Model depth: 5
    """

    type_: str = Field("CompilationAlbum", const=True, alias="@type")


if TYPE_CHECKING:

    CompilationAlbum.update_forward_refs()
