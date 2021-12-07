from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class RemixAlbum(MusicAlbumProductionType):
    """RemixAlbum.

    See https://schema.org/RemixAlbum.

    """
    type_: str = Field("RemixAlbum", const=True, alias='@type')
    

RemixAlbum.update_forward_refs()
