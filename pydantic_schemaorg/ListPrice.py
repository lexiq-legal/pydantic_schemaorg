from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class ListPrice(PriceTypeEnumeration):
    """Represents the list price (the price a product is actually advertised for) of an offered"
     "product.

    See: https://schema.org/ListPrice
    Model depth: 5
    """

    type_: str = Field("ListPrice", const=True, alias="@type")


if TYPE_CHECKING:

    ListPrice.update_forward_refs()
