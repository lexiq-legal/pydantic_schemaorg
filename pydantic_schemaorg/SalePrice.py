from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class SalePrice(PriceTypeEnumeration):
    """Represents a sale price (usually active for a limited period) of an offered product.

    See: https://schema.org/SalePrice
    Model depth: 5
    """

    type_: str = Field("SalePrice", const=True, alias="@type")


if TYPE_CHECKING:

    SalePrice.update_forward_refs()
