from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Review import Review


class UserReview(Review):
    """A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in contrast"
     "with [[CriticReview]].

    See: https://schema.org/UserReview
    Model depth: 4
    """
    type_: str = Field("UserReview", alias='@type')
    

