from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class GovernmentBuilding(CivicStructure):
    """A government building.

    See: https://schema.org/GovernmentBuilding
    Model depth: 4
    """

    type_: str = Field("GovernmentBuilding", const=True, alias="@type")


if TYPE_CHECKING:

    GovernmentBuilding.update_forward_refs()
