from pydantic import Field
from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType


class CompilationAlbum(MusicAlbumProductionType):
    """CompilationAlbum.

    See https://schema.org/CompilationAlbum.

    """
    type_: str = Field("CompilationAlbum", const=True, alias='@type')
    

CompilationAlbum.update_forward_refs()
