from pydantic import Field
from pydantic_schemaorg.Review import Review


class UserReview(Review):
    """A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in contrast"
     "with [[CriticReview]].

    See https://schema.org/UserReview.

    """
    type_: str = Field("UserReview", const=True, alias='@type')
    

UserReview.update_forward_refs()
