from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class StudioAlbum(MusicAlbumProductionType):
    """StudioAlbum.

    See https://schema.org/StudioAlbum.

    """

    locals().update({"@type": Field("StudioAlbum", const=True)})


StudioAlbum.update_forward_refs()
