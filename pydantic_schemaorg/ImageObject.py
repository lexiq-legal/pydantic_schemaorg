from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import StrictBool


from pydantic import Field
from pydantic_schemaorg.MediaObject import MediaObject


class ImageObject(MediaObject):
    """An image file.

    See: https://schema.org/ImageObject
    Model depth: 4
    """
    type_: str = Field("ImageObject", alias='@type')
    thumbnail: Optional[Union[List[Union['ImageObject', str]], 'ImageObject', str]] = Field(
        None,
        description="Thumbnail image for an image or video.",
    )
    embeddedTextCaption: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.",
    )
    representativeOfPage: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="Indicates whether this image is representative of the content of the page.",
    )
    exifData: Optional[Union[List[Union[str, 'Text', 'PropertyValue']], str, 'Text', 'PropertyValue']] = Field(
        None,
        description="exif data for this object.",
    )
    caption: Optional[Union[List[Union[str, 'Text', 'MediaObject']], str, 'Text', 'MediaObject']] = Field(
        None,
        description="The caption for this object. For downloadable machine formats (closed caption, subtitles"
     "etc.) use MediaObject and indicate the [[encodingFormat]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.MediaObject import MediaObject
