from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class RemixAlbum(MusicAlbumProductionType):
    """RemixAlbum.

    See https://schema.org/RemixAlbum.

    """

    locals().update({"@type": Field("RemixAlbum", const=True)})


RemixAlbum.update_forward_refs()
