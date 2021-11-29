from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class LiveAlbum(MusicAlbumProductionType):
    """LiveAlbum.

    See https://schema.org/LiveAlbum.

    """

    locals().update({"@type": Field("LiveAlbum", const=True)})


LiveAlbum.update_forward_refs()
