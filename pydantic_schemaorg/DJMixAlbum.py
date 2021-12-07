from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class DJMixAlbum(MusicAlbumProductionType):
    """DJMixAlbum.

    See https://schema.org/DJMixAlbum.

    """
    type_: str = Field("DJMixAlbum", const=True, alias='@type')
    

DJMixAlbum.update_forward_refs()
