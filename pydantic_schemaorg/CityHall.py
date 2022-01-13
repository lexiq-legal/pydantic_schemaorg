from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class CityHall(GovernmentBuilding):
    """A city hall.

    See: https://schema.org/CityHall
    Model depth: 5
    """

    type_: str = Field("CityHall", const=True, alias="@type")


if TYPE_CHECKING:

    CityHall.update_forward_refs()
