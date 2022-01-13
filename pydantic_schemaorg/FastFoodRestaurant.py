from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class FastFoodRestaurant(FoodEstablishment):
    """A fast-food restaurant.

    See: https://schema.org/FastFoodRestaurant
    Model depth: 5
    """

    type_: str = Field("FastFoodRestaurant", const=True, alias="@type")


if TYPE_CHECKING:

    FastFoodRestaurant.update_forward_refs()
