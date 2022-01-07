from pydantic import Field
from typing import List, Optional, Any, Union
from pydantic_schemaorg.Review import Review


class ClaimReview(Review):
    """A fact-checking review of claims made (or reported) in some creative work (referenced"
     "via itemReviewed).

    See https://schema.org/ClaimReview.

    """
    type_: str = Field("ClaimReview", const=True, alias='@type')
    claimReviewed: Optional[Union[List[str], str]] = Field(
        None,
        description="A short summary of the specific claims reviewed in a ClaimReview.",
    )
    

ClaimReview.update_forward_refs()
