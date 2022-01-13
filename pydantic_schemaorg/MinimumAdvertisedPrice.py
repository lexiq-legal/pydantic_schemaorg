from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration


class MinimumAdvertisedPrice(PriceTypeEnumeration):
    """Represents the minimum advertised price (\"MAP\") (as dictated by the manufacturer)"
     "of an offered product.

    See: https://schema.org/MinimumAdvertisedPrice
    Model depth: 5
    """

    type_: str = Field("MinimumAdvertisedPrice", const=True, alias="@type")


if TYPE_CHECKING:

    MinimumAdvertisedPrice.update_forward_refs()
