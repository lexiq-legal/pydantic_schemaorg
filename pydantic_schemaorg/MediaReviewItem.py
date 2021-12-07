from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.CreativeWork import CreativeWork


class MediaReviewItem(CreativeWork):
    """Represents an item or group of closely related items treated as a unit for the sake of evaluation"
     "in a [[MediaReview]]. Authorship etc. apply to the items rather than to the curation/grouping"
     "or reviewing party.

    See https://schema.org/MediaReviewItem.

    """
    type_: str = Field("MediaReviewItem", const=True, alias='@type')
    mediaItemAppearance: Any = Field(
        None,
        description="In the context of a [[MediaReview]], indicates specific media item(s) that are grouped"
     "using a [[MediaReviewItem]].",
    )
    

MediaReviewItem.update_forward_refs()
