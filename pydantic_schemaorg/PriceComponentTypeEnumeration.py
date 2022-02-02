from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class PriceComponentTypeEnumeration(Enumeration):
    """Enumerates different price components that together make up the total price for an offered"
     "product.

    See: https://schema.org/PriceComponentTypeEnumeration
    Model depth: 4
    """
    type_: str = Field("PriceComponentTypeEnumeration", alias='@type')
    

