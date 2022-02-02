from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class DJMixAlbum(MusicAlbumProductionType):
    """DJMixAlbum.

    See: https://schema.org/DJMixAlbum
    Model depth: 5
    """
    type_: str = Field("DJMixAlbum", alias='@type')
    

