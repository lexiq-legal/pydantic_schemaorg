from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Winery(FoodEstablishment):
    """A winery.

    See: https://schema.org/Winery
    Model depth: 5
    """

    type_: str = Field("Winery", const=True, alias="@type")


if TYPE_CHECKING:

    Winery.update_forward_refs()
