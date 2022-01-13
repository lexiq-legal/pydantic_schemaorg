from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Service import Service


class FoodService(Service):
    """A food service, like breakfast, lunch, or dinner.

    See: https://schema.org/FoodService
    Model depth: 4
    """

    type_: str = Field("FoodService", const=True, alias="@type")


if TYPE_CHECKING:

    FoodService.update_forward_refs()
