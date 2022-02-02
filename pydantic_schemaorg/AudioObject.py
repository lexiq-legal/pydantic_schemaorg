from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.MediaObject import MediaObject


class AudioObject(MediaObject):
    """An audio file.

    See: https://schema.org/AudioObject
    Model depth: 4
    """
    type_: str = Field("AudioObject", alias='@type')
    embeddedTextCaption: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.",
    )
    transcript: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="If this MediaObject is an AudioObject or VideoObject, the transcript of that object.",
    )
    caption: Optional[Union[List[Union[str, 'Text', 'MediaObject']], str, 'Text', 'MediaObject']] = Field(
        None,
        description="The caption for this object. For downloadable machine formats (closed caption, subtitles"
     "etc.) use MediaObject and indicate the [[encodingFormat]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MediaObject import MediaObject
