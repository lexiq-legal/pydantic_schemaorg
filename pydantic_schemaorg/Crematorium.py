from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class Crematorium(CivicStructure):
    """A crematorium.

    See: https://schema.org/Crematorium
    Model depth: 4
    """

    type_: str = Field("Crematorium", const=True, alias="@type")


if TYPE_CHECKING:

    Crematorium.update_forward_refs()
