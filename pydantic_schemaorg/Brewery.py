from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Brewery(FoodEstablishment):
    """Brewery.

    See: https://schema.org/Brewery
    Model depth: 5
    """

    type_: str = Field("Brewery", const=True, alias="@type")


if TYPE_CHECKING:

    Brewery.update_forward_refs()
