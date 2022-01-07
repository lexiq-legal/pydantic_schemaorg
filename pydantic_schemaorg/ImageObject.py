from pydantic import StrictBool, Field
from typing import List, Optional, Union
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.MediaObject import MediaObject


class ImageObject(MediaObject):
    """An image file.

    See https://schema.org/ImageObject.

    """
    type_: str = Field("ImageObject", const=True, alias='@type')
    thumbnail: Optional[Union[List[Union['ImageObject', str]], Union['ImageObject', str]]] = Field(
        None,
        description="Thumbnail image for an image or video.",
    )
    embeddedTextCaption: Optional[Union[List[str], str]] = Field(
        None,
        description="Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.",
    )
    representativeOfPage: Optional[Union[List[Union[StrictBool, str]], Union[StrictBool, str]]] = Field(
        None,
        description="Indicates whether this image is representative of the content of the page.",
    )
    exifData: Optional[Union[List[Union[str, PropertyValue]], Union[str, PropertyValue]]] = Field(
        None,
        description="exif data for this object.",
    )
    caption: Optional[Union[List[Union[str, MediaObject]], Union[str, MediaObject]]] = Field(
        None,
        description="The caption for this object. For downloadable machine formats (closed caption, subtitles"
     "etc.) use MediaObject and indicate the [[encodingFormat]].",
    )
    

ImageObject.update_forward_refs()
