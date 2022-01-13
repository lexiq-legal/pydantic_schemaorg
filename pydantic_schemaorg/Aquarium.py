from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class Aquarium(CivicStructure):
    """Aquarium.

    See: https://schema.org/Aquarium
    Model depth: 4
    """

    type_: str = Field("Aquarium", const=True, alias="@type")


if TYPE_CHECKING:

    Aquarium.update_forward_refs()
