from pydantic import Field
from pydantic_schema_org.PriceTypeEnumeration import PriceTypeEnumeration


class MinimumAdvertisedPrice(PriceTypeEnumeration):
    """Represents the minimum advertised price (\"MAP\") (as dictated by the manufacturer)"
     "of an offered product.

    See https://schema.org/MinimumAdvertisedPrice.

    """

    locals().update({"@type": Field("MinimumAdvertisedPrice", const=True)})


MinimumAdvertisedPrice.update_forward_refs()
