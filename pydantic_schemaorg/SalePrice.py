from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class SalePrice(PriceTypeEnumeration):
    """Represents a sale price (usually active for a limited period) of an offered product.

    See: https://schema.org/SalePrice
    Model depth: 5
    """
    type_: str = Field("SalePrice", alias='@type')
    

