from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class DemoAlbum(MusicAlbumProductionType):
    """DemoAlbum.

    See https://schema.org/DemoAlbum.

    """
    type_: str = Field("DemoAlbum", const=True, alias='@type')
    

DemoAlbum.update_forward_refs()
