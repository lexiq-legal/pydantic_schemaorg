from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class DigitalFormat(MusicReleaseFormatType):
    """DigitalFormat.

    See https://schema.org/DigitalFormat.

    """
    type_: str = Field("DigitalFormat", const=True, alias='@type')
    

DigitalFormat.update_forward_refs()
