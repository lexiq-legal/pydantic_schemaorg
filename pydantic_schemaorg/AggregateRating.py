from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Rating import Rating


class AggregateRating(Rating):
    """The average rating based on multiple ratings or reviews.

    See https://schema.org/AggregateRating.

    """
    type_: str = Field("AggregateRating", const=True, alias='@type')
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
    

AggregateRating.update_forward_refs()
