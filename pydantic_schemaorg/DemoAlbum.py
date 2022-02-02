from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class DemoAlbum(MusicAlbumProductionType):
    """DemoAlbum.

    See: https://schema.org/DemoAlbum
    Model depth: 5
    """
    type_: str = Field("DemoAlbum", alias='@type')
    

