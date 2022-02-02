from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class ListPrice(PriceTypeEnumeration):
    """Represents the list price (the price a product is actually advertised for) of an offered"
     "product.

    See: https://schema.org/ListPrice
    Model depth: 5
    """
    type_: str = Field("ListPrice", alias='@type')
    

