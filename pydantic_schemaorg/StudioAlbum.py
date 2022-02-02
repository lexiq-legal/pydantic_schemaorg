from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class StudioAlbum(MusicAlbumProductionType):
    """StudioAlbum.

    See: https://schema.org/StudioAlbum
    Model depth: 5
    """
    type_: str = Field("StudioAlbum", alias='@type')
    

