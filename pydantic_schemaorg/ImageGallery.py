from pydantic import Field
from pydantic_schemaorg.MediaGallery import MediaGallery


class ImageGallery(MediaGallery):
    """Web page type: Image gallery page.

    See https://schema.org/ImageGallery.

    """
    type_: str = Field("ImageGallery", const=True, alias='@type')
    

ImageGallery.update_forward_refs()
