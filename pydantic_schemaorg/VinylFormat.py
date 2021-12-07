from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class VinylFormat(MusicReleaseFormatType):
    """VinylFormat.

    See https://schema.org/VinylFormat.

    """
    type_: str = Field("VinylFormat", const=True, alias='@type')
    

VinylFormat.update_forward_refs()
