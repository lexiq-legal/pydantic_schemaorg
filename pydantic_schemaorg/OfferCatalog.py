from pydantic import Field
from pydantic_schemaorg.ItemList import ItemList


class OfferCatalog(ItemList):
    """An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs"
     "that are offeredBy the same provider.

    See https://schema.org/OfferCatalog.

    """

    locals().update({"@type": Field("OfferCatalog", const=True)})


OfferCatalog.update_forward_refs()
