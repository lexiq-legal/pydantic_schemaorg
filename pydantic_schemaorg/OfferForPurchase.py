from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Offer import Offer


class OfferForPurchase(Offer):
    """An [[OfferForPurchase]] in Schema.org represents an [[Offer]] to sell something,"
     "i.e. an [[Offer]] whose [[businessFunction]] is [sell](http://purl.org/goodrelations/v1#Sell.)."
     "See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for background"
     "on the underlying concepts.

    See: https://schema.org/OfferForPurchase
    Model depth: 4
    """
    type_: str = Field("OfferForPurchase", alias='@type')
    

