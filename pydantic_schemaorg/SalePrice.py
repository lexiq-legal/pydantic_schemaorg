from pydantic import Field
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class SalePrice(PriceTypeEnumeration):
    """Represents a sale price (usually active for a limited period) of an offered product.

    See https://schema.org/SalePrice.

    """

    locals().update({"@type": Field("SalePrice", const=True)})


SalePrice.update_forward_refs()
