from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.CreativeWork import CreativeWork


class Review(CreativeWork):
    """A review of an item - for example, of a restaurant, movie, or store.

    See https://schema.org/Review.

    """

    associatedMediaReview: Any = Field(
        None,
        description="An associated [[MediaReview]], related by specific common content, topic or claim."
     "The expectation is that this property would be most typically used in cases where a single"
     "activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]]"
     "would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be"
     "used on [[MediaReview]].",
    )
    positiveNotes: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="Indicates, in the context of a [[Review]] (e.g. framed as 'pro' vs 'con' considerations),"
     "positive considerations - either as unstructured text, or a list.",
    )
    reviewAspect: Optional[Union[List[str], str]] = Field(
        None,
        description="This Review or Rating is relevant to this part or facet of the itemReviewed.",
    )
    reviewRating: Any = Field(
        None,
        description="The rating given in this review. Note that reviews can themselves be rated. The ```reviewRating```"
     "applies to rating given by the review. The [[aggregateRating]] property applies to"
     "the review itself, as a creative work.",
    )
    associatedClaimReview: Any = Field(
        None,
        description="An associated [[ClaimReview]], related by specific common content, topic or claim."
     "The expectation is that this property would be most typically used in cases where a single"
     "activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]]"
     "would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be"
     "used on [[MediaReview]].",
    )
    associatedReview: Any = Field(
        None,
        description="An associated [[Review]].",
    )
    reviewBody: Optional[Union[List[str], str]] = Field(
        None,
        description="The actual body of the review.",
    )
    negativeNotes: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="Indicates, in the context of a [[Review]] (e.g. framed as 'pro' vs 'con' considerations),"
     "negative considerations - either as unstructured text, or a list.",
    )
    itemReviewed: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="The item that is being reviewed/rated.",
    )
    locals().update({"@type": Field("Review", const=True)})


Review.update_forward_refs()
