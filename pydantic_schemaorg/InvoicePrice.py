from pydantic import Field
from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class InvoicePrice(PriceTypeEnumeration):
    """Represents the invoice price of an offered product.

    See https://schema.org/InvoicePrice.

    """
    type_: str = Field("InvoicePrice", const=True, alias='@type')
    

InvoicePrice.update_forward_refs()
