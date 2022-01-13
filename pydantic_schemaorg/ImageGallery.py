from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.MediaGallery import MediaGallery


class ImageGallery(MediaGallery):
    """Web page type: Image gallery page.

    See: https://schema.org/ImageGallery
    Model depth: 6
    """

    type_: str = Field("ImageGallery", const=True, alias="@type")


if TYPE_CHECKING:

    ImageGallery.update_forward_refs()
