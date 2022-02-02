from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.MediaObject import MediaObject


class VideoObject(MediaObject):
    """A video file.

    See: https://schema.org/VideoObject
    Model depth: 4
    """
    type_: str = Field("VideoObject", alias='@type')
    actors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    thumbnail: Optional[Union[List[Union['ImageObject', str]], 'ImageObject', str]] = Field(
        None,
        description="Thumbnail image for an image or video.",
    )
    embeddedTextCaption: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.",
    )
    videoQuality: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The quality of the video.",
    )
    director: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",
    )
    videoFrameSize: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The frame size of the video.",
    )
    actor: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    directors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated"
     "with individual items or with a series, episode, clip.",
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
    musicBy: Optional[Union[List[Union['MusicGroup', 'Person', str]], 'MusicGroup', 'Person', str]] = Field(
        None,
        description="The composer of the soundtrack.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MediaObject import MediaObject
    from pydantic_schemaorg.MusicGroup import MusicGroup
