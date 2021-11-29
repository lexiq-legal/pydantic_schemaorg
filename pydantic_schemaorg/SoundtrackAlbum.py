from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class SoundtrackAlbum(MusicAlbumProductionType):
    """SoundtrackAlbum.

    See https://schema.org/SoundtrackAlbum.

    """

    locals().update({"@type": Field("SoundtrackAlbum", const=True)})


SoundtrackAlbum.update_forward_refs()
