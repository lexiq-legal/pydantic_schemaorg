from pydantic import Field
from pydantic_schemaorg.MediaGallery import MediaGallery


class VideoGallery(MediaGallery):
    """Web page type: Video gallery page.

    See https://schema.org/VideoGallery.

    """
    type_: str = Field("VideoGallery", const=True, alias='@type')
    

VideoGallery.update_forward_refs()
