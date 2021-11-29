from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person


class Claim(CreativeWork):
    """A [[Claim]] in Schema.org represents a specific, factually-oriented claim that could"
     "be the [[itemReviewed]] in a [[ClaimReview]]. The content of a claim can be summarized"
     "with the [[text]] property. Variations on well known claims can have their common identity"
     "indicated via [[sameAs]] links, and summarized with a [[name]]. Ideally, a [[Claim]]"
     "description includes enough contextual information to minimize the risk of ambiguity"
     "or inclarity. In practice, many claims are better understood in the context in which"
     "they appear or the interpretations provided by claim reviews. Beyond [[ClaimReview]],"
     "the Claim type can be associated with related creative works - for example a [[ScholarlyArticle]]"
     "or [[Question]] might be [[about]] some [[Claim]]. At this time, Schema.org does not"
     "define any types of relationship between claims. This is a natural area for future exploration.

    See https://schema.org/Claim.

    """

    firstAppearance: Optional[Union[List[CreativeWork], CreativeWork]] = Field(
        None,
        description="Indicates the first known occurence of a [[Claim]] in some [[CreativeWork]].",
    )
    claimInterpreter: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="For a [[Claim]] interpreted from [[MediaObject]] content sed to indicate a claim contained,"
     "implied or refined from the content of a [[MediaObject]].",
    )
    appearance: Optional[Union[List[CreativeWork], CreativeWork]] = Field(
        None,
        description="Indicates an occurence of a [[Claim]] in some [[CreativeWork]].",
    )
    locals().update({"@type": Field("Claim", const=True)})


Claim.update_forward_refs()
