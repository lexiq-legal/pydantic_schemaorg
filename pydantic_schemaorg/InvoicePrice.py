from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class InvoicePrice(PriceTypeEnumeration):
    """Represents the invoice price of an offered product.

    See: https://schema.org/InvoicePrice
    Model depth: 5
    """

    type_: str = Field("InvoicePrice", const=True, alias="@type")


if TYPE_CHECKING:

    InvoicePrice.update_forward_refs()
