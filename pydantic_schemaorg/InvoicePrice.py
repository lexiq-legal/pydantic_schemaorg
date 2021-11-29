from pydantic import Field
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class InvoicePrice(PriceTypeEnumeration):
    """Represents the invoice price of an offered product.

    See https://schema.org/InvoicePrice.

    """

    locals().update({"@type": Field("InvoicePrice", const=True)})


InvoicePrice.update_forward_refs()
