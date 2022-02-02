from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class MixtapeAlbum(MusicAlbumProductionType):
    """MixtapeAlbum.

    See: https://schema.org/MixtapeAlbum
    Model depth: 5
    """
    type_: str = Field("MixtapeAlbum", alias='@type')
    

