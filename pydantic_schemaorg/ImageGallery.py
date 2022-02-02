from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MediaGallery import MediaGallery


class ImageGallery(MediaGallery):
    """Web page type: Image gallery page.

    See: https://schema.org/ImageGallery
    Model depth: 6
    """
    type_: str = Field("ImageGallery", alias='@type')
    

