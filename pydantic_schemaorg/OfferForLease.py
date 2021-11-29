from pydantic import Field
from pydantic_schemaorg.Offer import Offer


class OfferForLease(Offer):
    """An [[OfferForLease]] in Schema.org represents an [[Offer]] to lease out something,"
     "i.e. an [[Offer]] whose [[businessFunction]] is [lease out](http://purl.org/goodrelations/v1#LeaseOut.)."
     "See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for background"
     "on the underlying concepts.

    See https://schema.org/OfferForLease.

    """

    locals().update({"@type": Field("OfferForLease", const=True)})


OfferForLease.update_forward_refs()
