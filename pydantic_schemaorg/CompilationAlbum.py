from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class CompilationAlbum(MusicAlbumProductionType):
    """CompilationAlbum.

    See: https://schema.org/CompilationAlbum
    Model depth: 5
    """
    type_: str = Field("CompilationAlbum", alias='@type')
    

