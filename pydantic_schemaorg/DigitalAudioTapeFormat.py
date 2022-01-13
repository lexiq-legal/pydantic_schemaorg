from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType


class DigitalAudioTapeFormat(MusicReleaseFormatType):
    """DigitalAudioTapeFormat.

    See: https://schema.org/DigitalAudioTapeFormat
    Model depth: 5
    """

    type_: str = Field("DigitalAudioTapeFormat", const=True, alias="@type")


if TYPE_CHECKING:

    DigitalAudioTapeFormat.update_forward_refs()
