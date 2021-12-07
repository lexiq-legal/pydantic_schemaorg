from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class MixtapeAlbum(MusicAlbumProductionType):
    """MixtapeAlbum.

    See https://schema.org/MixtapeAlbum.

    """
    type_: str = Field("MixtapeAlbum", const=True, alias='@type')
    

MixtapeAlbum.update_forward_refs()
