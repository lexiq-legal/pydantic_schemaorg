from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Review import Review


class ClaimReview(Review):
    """A fact-checking review of claims made (or reported) in some creative work (referenced"
     "via itemReviewed).

    See https://schema.org/ClaimReview.

    """

    claimReviewed: Optional[Union[List[str], str]] = Field(
        None,
        description="A short summary of the specific claims reviewed in a ClaimReview.",
    )
    locals().update({"@type": Field("ClaimReview", const=True)})


ClaimReview.update_forward_refs()
