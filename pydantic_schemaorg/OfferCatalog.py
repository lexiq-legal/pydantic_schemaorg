from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ItemList import ItemList


class OfferCatalog(ItemList):
    """An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs"
     "that are offeredBy the same provider.

    See: https://schema.org/OfferCatalog
    Model depth: 4
    """
    type_: str = Field("OfferCatalog", alias='@type')
    

