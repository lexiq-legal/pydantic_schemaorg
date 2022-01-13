from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class CafeOrCoffeeShop(FoodEstablishment):
    """A cafe or coffee shop.

    See: https://schema.org/CafeOrCoffeeShop
    Model depth: 5
    """

    type_: str = Field("CafeOrCoffeeShop", const=True, alias="@type")


if TYPE_CHECKING:

    CafeOrCoffeeShop.update_forward_refs()
