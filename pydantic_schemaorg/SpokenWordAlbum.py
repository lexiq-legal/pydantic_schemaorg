from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class SpokenWordAlbum(MusicAlbumProductionType):
    """SpokenWordAlbum.

    See https://schema.org/SpokenWordAlbum.

    """
    type_: str = Field("SpokenWordAlbum", const=True, alias='@type')
    

SpokenWordAlbum.update_forward_refs()
