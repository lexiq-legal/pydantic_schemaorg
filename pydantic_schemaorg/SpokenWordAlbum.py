from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class SpokenWordAlbum(MusicAlbumProductionType):
    """SpokenWordAlbum.

    See https://schema.org/SpokenWordAlbum.

    """

    locals().update({"@type": Field("SpokenWordAlbum", const=True)})


SpokenWordAlbum.update_forward_refs()
