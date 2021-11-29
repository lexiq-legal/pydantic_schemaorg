from pydantic import Field
from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class DigitalAudioTapeFormat(MusicReleaseFormatType):
    """DigitalAudioTapeFormat.

    See https://schema.org/DigitalAudioTapeFormat.

    """

    locals().update({"@type": Field("DigitalAudioTapeFormat", const=True)})


DigitalAudioTapeFormat.update_forward_refs()
