from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MediaGallery import MediaGallery


class VideoGallery(MediaGallery):
    """Web page type: Video gallery page.

    See: https://schema.org/VideoGallery
    Model depth: 6
    """
    type_: str = Field("VideoGallery", alias='@type')
    

