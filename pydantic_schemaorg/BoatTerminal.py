from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class BoatTerminal(CivicStructure):
    """A terminal for boats, ships, and other water vessels.

    See: https://schema.org/BoatTerminal
    Model depth: 4
    """

    type_: str = Field("BoatTerminal", const=True, alias="@type")


if TYPE_CHECKING:

    BoatTerminal.update_forward_refs()
