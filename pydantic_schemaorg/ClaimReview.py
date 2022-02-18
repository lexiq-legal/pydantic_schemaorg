from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Review import Review


class ClaimReview(Review):
    """A fact-checking review of claims made (or reported) in some creative work (referenced"
     "via itemReviewed).

    See: https://schema.org/ClaimReview
    Model depth: 4
    """
    type_: str = Field(default="ClaimReview", alias='@type', const=True)
    claimReviewed: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A short summary of the specific claims reviewed in a ClaimReview.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
