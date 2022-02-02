from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class MinimumAdvertisedPrice(PriceTypeEnumeration):
    """Represents the minimum advertised price (\"MAP\") (as dictated by the manufacturer)"
     "of an offered product.

    See: https://schema.org/MinimumAdvertisedPrice
    Model depth: 5
    """
    type_: str = Field("MinimumAdvertisedPrice", alias='@type')
    

