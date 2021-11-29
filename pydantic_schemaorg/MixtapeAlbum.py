from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class MixtapeAlbum(MusicAlbumProductionType):
    """MixtapeAlbum.

    See https://schema.org/MixtapeAlbum.

    """

    locals().update({"@type": Field("MixtapeAlbum", const=True)})


MixtapeAlbum.update_forward_refs()
