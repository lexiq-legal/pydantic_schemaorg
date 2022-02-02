from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class CDFormat(MusicReleaseFormatType):
    """CDFormat.

    See: https://schema.org/CDFormat
    Model depth: 5
    """
    type_: str = Field("CDFormat", alias='@type')
    

