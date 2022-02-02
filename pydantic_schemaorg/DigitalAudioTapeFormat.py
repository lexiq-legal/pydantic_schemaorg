from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class DigitalAudioTapeFormat(MusicReleaseFormatType):
    """DigitalAudioTapeFormat.

    See: https://schema.org/DigitalAudioTapeFormat
    Model depth: 5
    """
    type_: str = Field("DigitalAudioTapeFormat", alias='@type')
    

