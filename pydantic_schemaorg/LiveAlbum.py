from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class LiveAlbum(MusicAlbumProductionType):
    """LiveAlbum.

    See: https://schema.org/LiveAlbum
    Model depth: 5
    """
    type_: str = Field("LiveAlbum", alias='@type')
    

