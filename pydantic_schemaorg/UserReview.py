from pydantic import Field
from pydantic_schemaorg.Review import Review


class UserReview(Review):
    """A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in contrast"
     "with [[CriticReview]].

    See https://schema.org/UserReview.

    """

    locals().update({"@type": Field("UserReview", const=True)})


UserReview.update_forward_refs()
