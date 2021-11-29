from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.MediaObject import MediaObject


class AudioObject(MediaObject):
    """An audio file.

    See https://schema.org/AudioObject.

    """

    embeddedTextCaption: Optional[Union[List[str], str]] = Field(
        None,
        description="Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.",
    )
    transcript: Optional[Union[List[str], str]] = Field(
        None,
        description="If this MediaObject is an AudioObject or VideoObject, the transcript of that object.",
    )
    caption: Optional[Union[List[Union[str, MediaObject]], Union[str, MediaObject]]] = Field(
        None,
        description="The caption for this object. For downloadable machine formats (closed caption, subtitles"
     "etc.) use MediaObject and indicate the [[encodingFormat]].",
    )
    locals().update({"@type": Field("AudioObject", const=True)})


AudioObject.update_forward_refs()
