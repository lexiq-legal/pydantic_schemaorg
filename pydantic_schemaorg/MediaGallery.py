from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CollectionPage import CollectionPage


class MediaGallery(CollectionPage):
    """Web page type: Media gallery page. A mixed-media page that can contains media such as"
     "images, videos, and other multimedia.

    See: https://schema.org/MediaGallery
    Model depth: 5
    """

    type_: str = Field("MediaGallery", const=True, alias="@type")


if TYPE_CHECKING:

    MediaGallery.update_forward_refs()
