from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class MediaReviewItem(CreativeWork):
    """Represents an item or group of closely related items treated as a unit for the sake of evaluation"
     "in a [[MediaReview]]. Authorship etc. apply to the items rather than to the curation/grouping"
     "or reviewing party.

    See: https://schema.org/MediaReviewItem
    Model depth: 3
    """
    type_: str = Field(default="MediaReviewItem", alias='@type', const=True)
    mediaItemAppearance: Optional[Union[List[Union['MediaObject', str]], 'MediaObject', str]] = Field(
        default=None,
        description="In the context of a [[MediaReview]], indicates specific media item(s) that are grouped"
     "using a [[MediaReviewItem]].",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MediaObject import MediaObject
