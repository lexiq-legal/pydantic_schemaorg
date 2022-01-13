from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.FoodEstablishment import FoodEstablishment


class Distillery(FoodEstablishment):
    """A distillery.

    See: https://schema.org/Distillery
    Model depth: 5
    """

    type_: str = Field("Distillery", const=True, alias="@type")


if TYPE_CHECKING:

    Distillery.update_forward_refs()
