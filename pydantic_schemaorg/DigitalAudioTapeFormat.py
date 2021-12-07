from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class DigitalAudioTapeFormat(MusicReleaseFormatType):
    """DigitalAudioTapeFormat.

    See https://schema.org/DigitalAudioTapeFormat.

    """
    type_: str = Field("DigitalAudioTapeFormat", const=True, alias='@type')
    

DigitalAudioTapeFormat.update_forward_refs()
