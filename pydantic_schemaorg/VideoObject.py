from pydantic import Field
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.ImageObject import ImageObject
from pydantic_schemaorg.MediaObject import MediaObject


class VideoObject(MediaObject):
    """A video file.

    See https://schema.org/VideoObject.

    """

    actors: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    thumbnail: Optional[Union[List[ImageObject], ImageObject]] = Field(
        None,
        description="Thumbnail image for an image or video.",
    )
    embeddedTextCaption: Optional[Union[List[str], str]] = Field(
        None,
        description="Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.",
    )
    videoQuality: Optional[Union[List[str], str]] = Field(
        None,
        description="The quality of the video.",
    )
    director: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",
    )
    videoFrameSize: Optional[Union[List[str], str]] = Field(
        None,
        description="The frame size of the video.",
    )
    actor: Optional[Union[List[Person], Person]] = Field(
        None,
        description="An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    directors: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated"
     "with individual items or with a series, episode, clip.",
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
    musicBy: Union[List[Union[Person, Any]], Union[Person, Any]] = Field(
        None,
        description="The composer of the soundtrack.",
    )
    locals().update({"@type": Field("VideoObject", const=True)})


VideoObject.update_forward_refs()
