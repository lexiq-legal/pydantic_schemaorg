from pydantic import Field
from pydantic_schema_org.PriceTypeEnumeration import PriceTypeEnumeration


class ListPrice(PriceTypeEnumeration):
    """Represents the list price (the price a product is actually advertised for) of an offered"
     "product.

    See https://schema.org/ListPrice.

    """

    locals().update({"@type": Field("ListPrice", const=True)})


ListPrice.update_forward_refs()
