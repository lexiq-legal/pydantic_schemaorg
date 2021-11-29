from pydantic import Field
from pydantic_schema_org.Review import Review
from typing import Any, Optional, Union, List
from pydantic_schema_org.AssessAction import AssessAction


class ReviewAction(AssessAction):
    """The act of producing a balanced opinion about the object for an audience. An agent reviews"
     "an object with participants resulting in a review.

    See https://schema.org/ReviewAction.

    """

    resultReview: Optional[Union[List[Review], Review]] = Field(
        None,
        description="A sub property of result. The review that resulted in the performing of the action.",
    )
    locals().update({"@type": Field("ReviewAction", const=True)})


ReviewAction.update_forward_refs()
