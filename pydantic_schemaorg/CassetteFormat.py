from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class CassetteFormat(MusicReleaseFormatType):
    """CassetteFormat.

    See: https://schema.org/CassetteFormat
    Model depth: 5
    """
    type_: str = Field("CassetteFormat", alias='@type')
    

