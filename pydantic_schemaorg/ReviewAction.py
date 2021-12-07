from pydantic import Field
from pydantic_schemaorg.Review import Review
from typing import Any, Optional, Union, List
from pydantic_schemaorg.AssessAction import AssessAction


class ReviewAction(AssessAction):
    """The act of producing a balanced opinion about the object for an audience. An agent reviews"
     "an object with participants resulting in a review.

    See https://schema.org/ReviewAction.

    """
    type_: str = Field("ReviewAction", const=True, alias='@type')
    resultReview: Optional[Union[List[Review], Review]] = Field(
        None,
        description="A sub property of result. The review that resulted in the performing of the action.",
    )
    

ReviewAction.update_forward_refs()
