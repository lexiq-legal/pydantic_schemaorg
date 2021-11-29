from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Rating import Rating


class AggregateRating(Rating):
    """The average rating based on multiple ratings or reviews.

    See https://schema.org/AggregateRating.

    """

    reviewCount: Optional[Union[List[int], int]] = Field(
        None,
        description="The count of total number of reviews.",
    )
    ratingCount: Optional[Union[List[int], int]] = Field(
        None,
        description="The count of total number of ratings.",
    )
    itemReviewed: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="The item that is being reviewed/rated.",
    )
    locals().update({"@type": Field("AggregateRating", const=True)})


AggregateRating.update_forward_refs()
