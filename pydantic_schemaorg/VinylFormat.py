from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class VinylFormat(MusicReleaseFormatType):
    """VinylFormat.

    See: https://schema.org/VinylFormat
    Model depth: 5
    """
    type_: str = Field("VinylFormat", alias='@type')
    

