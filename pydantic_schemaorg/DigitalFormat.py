from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class DigitalFormat(MusicReleaseFormatType):
    """DigitalFormat.

    See: https://schema.org/DigitalFormat
    Model depth: 5
    """
    type_: str = Field("DigitalFormat", alias='@type')
    

