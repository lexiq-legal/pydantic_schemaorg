from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation

from pydantic_schemaorg.CivicStructure import CivicStructure


class StadiumOrArena(SportsActivityLocation, CivicStructure):
    """A stadium.

    See: https://schema.org/StadiumOrArena
    Model depth: 4
    """

    type_: str = Field("StadiumOrArena", const=True, alias="@type")


if TYPE_CHECKING:

    StadiumOrArena.update_forward_refs()
