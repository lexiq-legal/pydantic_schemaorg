from pydantic import Field
from pydantic_schemaorg.MediaGallery import MediaGallery


class VideoGallery(MediaGallery):
    """Web page type: Video gallery page.

    See https://schema.org/VideoGallery.

    """

    locals().update({"@type": Field("VideoGallery", const=True)})


VideoGallery.update_forward_refs()
