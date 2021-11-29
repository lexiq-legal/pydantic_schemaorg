from pydantic import Field
from pydantic_schemaorg.MediaGallery import MediaGallery


class ImageGallery(MediaGallery):
    """Web page type: Image gallery page.

    See https://schema.org/ImageGallery.

    """

    locals().update({"@type": Field("ImageGallery", const=True)})


ImageGallery.update_forward_refs()
