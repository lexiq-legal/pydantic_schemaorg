from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class SoundtrackAlbum(MusicAlbumProductionType):
    """SoundtrackAlbum.

    See https://schema.org/SoundtrackAlbum.

    """
    type_: str = Field("SoundtrackAlbum", const=True, alias='@type')
    

SoundtrackAlbum.update_forward_refs()
