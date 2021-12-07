from pydantic import Field
from pydantic_schemaorg.Review import Review


class EmployerReview(Review):
    """An [[EmployerReview]] is a review of an [[Organization]] regarding its role as an employer,"
     "written by a current or former employee of that organization.

    See https://schema.org/EmployerReview.

    """
    type_: str = Field("EmployerReview", const=True, alias='@type')
    

EmployerReview.update_forward_refs()
