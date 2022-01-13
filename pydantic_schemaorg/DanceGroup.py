from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PerformingGroup import PerformingGroup


class DanceGroup(PerformingGroup):
    """A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.

    See: https://schema.org/DanceGroup
    Model depth: 4
    """

    type_: str = Field("DanceGroup", const=True, alias="@type")


if TYPE_CHECKING:

    DanceGroup.update_forward_refs()
