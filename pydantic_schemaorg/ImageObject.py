from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import StrictBool


from pydantic import Field
from pydantic_schemaorg.MediaObject import MediaObject


class ImageObject(MediaObject):
    """An image file.

    See: https://schema.org/ImageObject
    Model depth: 4
    """
    type_: str = Field(default="ImageObject", alias='@type', constant=True)
    thumbnail: Optional[Union[List[Union['ImageObject', str]], 'ImageObject', str]] = Field(
        default=None,
        description="Thumbnail image for an image or video.",
    )
    embeddedTextCaption: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.",
    )
    representativeOfPage: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Indicates whether this image is representative of the content of the page.",
    )
    exifData: Optional[Union[List[Union[str, 'Text', 'PropertyValue']], str, 'Text', 'PropertyValue']] = Field(
        default=None,
        description="exif data for this object.",
    )
    caption: Optional[Union[List[Union[str, 'Text', 'MediaObject']], str, 'Text', 'MediaObject']] = Field(
        default=None,
        description="The caption for this object. For downloadable machine formats (closed caption, subtitles"
     "etc.) use MediaObject and indicate the [[encodingFormat]].",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.MediaObject import MediaObject
