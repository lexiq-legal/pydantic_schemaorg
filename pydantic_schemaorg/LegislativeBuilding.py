from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.GovernmentBuilding import GovernmentBuilding


class LegislativeBuilding(GovernmentBuilding):
    """A legislative building&#x2014;for example, the state capitol.

    See: https://schema.org/LegislativeBuilding
    Model depth: 5
    """

    type_: str = Field("LegislativeBuilding", const=True, alias="@type")


if TYPE_CHECKING:

    LegislativeBuilding.update_forward_refs()
