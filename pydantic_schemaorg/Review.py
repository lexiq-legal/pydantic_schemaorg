from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Review(CreativeWork):
    """A review of an item - for example, of a restaurant, movie, or store.

    See: https://schema.org/Review
    Model depth: 3
    """
    type_: str = Field("Review", alias='@type')
    associatedMediaReview: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        None,
        description="An associated [[MediaReview]], related by specific common content, topic or claim."
     "The expectation is that this property would be most typically used in cases where a single"
     "activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]]"
     "would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be"
     "used on [[MediaReview]].",
    )
    positiveNotes: Optional[Union[List[Union[str, 'Text', 'WebContent', 'ListItem', 'ItemList']], str, 'Text', 'WebContent', 'ListItem', 'ItemList']] = Field(
        None,
        description="Indicates, in the context of a [[Review]] (e.g. framed as 'pro' vs 'con' considerations),"
     "positive considerations - either as unstructured text, or a list.",
    )
    reviewAspect: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="This Review or Rating is relevant to this part or facet of the itemReviewed.",
    )
    reviewRating: Optional[Union[List[Union['Rating', str]], 'Rating', str]] = Field(
        None,
        description="The rating given in this review. Note that reviews can themselves be rated. The ```reviewRating```"
     "applies to rating given by the review. The [[aggregateRating]] property applies to"
     "the review itself, as a creative work.",
    )
    associatedClaimReview: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        None,
        description="An associated [[ClaimReview]], related by specific common content, topic or claim."
     "The expectation is that this property would be most typically used in cases where a single"
     "activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]]"
     "would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be"
     "used on [[MediaReview]].",
    )
    associatedReview: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        None,
        description="An associated [[Review]].",
    )
    reviewBody: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The actual body of the review.",
    )
    negativeNotes: Optional[Union[List[Union[str, 'Text', 'WebContent', 'ListItem', 'ItemList']], str, 'Text', 'WebContent', 'ListItem', 'ItemList']] = Field(
        None,
        description="Indicates, in the context of a [[Review]] (e.g. framed as 'pro' vs 'con' considerations),"
     "negative considerations - either as unstructured text, or a list.",
    )
    itemReviewed: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        None,
        description="The item that is being reviewed/rated.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.WebContent import WebContent
    from pydantic_schemaorg.ListItem import ListItem
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.Rating import Rating
    from pydantic_schemaorg.Thing import Thing
