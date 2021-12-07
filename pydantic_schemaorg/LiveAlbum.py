from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class LiveAlbum(MusicAlbumProductionType):
    """LiveAlbum.

    See https://schema.org/LiveAlbum.

    """
    type_: str = Field("LiveAlbum", const=True, alias='@type')
    

LiveAlbum.update_forward_refs()
