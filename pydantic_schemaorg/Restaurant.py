from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Restaurant(FoodEstablishment):
    """A restaurant.

    See: https://schema.org/Restaurant
    Model depth: 5
    """

    type_: str = Field("Restaurant", const=True, alias="@type")


if TYPE_CHECKING:

    Restaurant.update_forward_refs()
