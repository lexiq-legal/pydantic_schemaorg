from pydantic import Field
from pydantic_schema_org.MusicAlbumProductionType import MusicAlbumProductionType


class DemoAlbum(MusicAlbumProductionType):
    """DemoAlbum.

    See https://schema.org/DemoAlbum.

    """

    locals().update({"@type": Field("DemoAlbum", const=True)})


DemoAlbum.update_forward_refs()
