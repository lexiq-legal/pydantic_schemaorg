from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class DVDFormat(MusicReleaseFormatType):
    """DVDFormat.

    See https://schema.org/DVDFormat.

    """
    type_: str = Field("DVDFormat", const=True, alias='@type')
    

DVDFormat.update_forward_refs()
