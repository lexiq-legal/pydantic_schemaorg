from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class IceCreamShop(FoodEstablishment):
    """An ice cream shop.

    See: https://schema.org/IceCreamShop
    Model depth: 5
    """

    type_: str = Field("IceCreamShop", const=True, alias="@type")


if TYPE_CHECKING:

    IceCreamShop.update_forward_refs()
