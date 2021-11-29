from pydantic import Field
from pydantic_schemaorg.Review import Review


class CriticReview(Review):
    """A [[CriticReview]] is a more specialized form of Review written or published by a source"
     "that is recognized for its reviewing activities. These can include online columns,"
     "travel and food guides, TV and radio shows, blogs and other independent Web sites. [[CriticReview]]s"
     "are typically more in-depth and professionally written. For simpler, casually written"
     "user/visitor/viewer/customer reviews, it is more appropriate to use the [[UserReview]]"
     "type. Review aggregator sites such as Metacritic already separate out the site's user"
     "reviews from selected critic reviews that originate from third-party sources.

    See https://schema.org/CriticReview.

    """

    locals().update({"@type": Field("CriticReview", const=True)})


CriticReview.update_forward_refs()
