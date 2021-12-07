from pydantic import Field
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class SalePrice(PriceTypeEnumeration):
    """Represents a sale price (usually active for a limited period) of an offered product.

    See https://schema.org/SalePrice.

    """
    type_: str = Field("SalePrice", const=True, alias='@type')
    

SalePrice.update_forward_refs()
