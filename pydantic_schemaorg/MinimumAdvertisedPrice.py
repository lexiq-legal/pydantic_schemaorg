from pydantic import Field
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class MinimumAdvertisedPrice(PriceTypeEnumeration):
    """Represents the minimum advertised price (\"MAP\") (as dictated by the manufacturer)"
     "of an offered product.

    See https://schema.org/MinimumAdvertisedPrice.

    """
    type_: str = Field("MinimumAdvertisedPrice", const=True, alias='@type')
    

MinimumAdvertisedPrice.update_forward_refs()
