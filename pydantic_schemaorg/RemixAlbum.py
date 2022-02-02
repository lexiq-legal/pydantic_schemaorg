from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class RemixAlbum(MusicAlbumProductionType):
    """RemixAlbum.

    See: https://schema.org/RemixAlbum
    Model depth: 5
    """
    type_: str = Field("RemixAlbum", alias='@type')
    

