from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Review import Review


class EmployerReview(Review):
    """An [[EmployerReview]] is a review of an [[Organization]] regarding its role as an employer,"
     "written by a current or former employee of that organization.

    See: https://schema.org/EmployerReview
    Model depth: 4
    """
    type_: str = Field("EmployerReview", alias='@type')
    

