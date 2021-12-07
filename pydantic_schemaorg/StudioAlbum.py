from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class StudioAlbum(MusicAlbumProductionType):
    """StudioAlbum.

    See https://schema.org/StudioAlbum.

    """
    type_: str = Field("StudioAlbum", const=True, alias='@type')
    

StudioAlbum.update_forward_refs()
