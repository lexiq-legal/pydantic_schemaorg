from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class DVDFormat(MusicReleaseFormatType):
    """DVDFormat.

    See: https://schema.org/DVDFormat
    Model depth: 5
    """
    type_: str = Field("DVDFormat", alias='@type')
    

