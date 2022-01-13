from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class Playground(CivicStructure):
    """A playground.

    See: https://schema.org/Playground
    Model depth: 4
    """

    type_: str = Field("Playground", const=True, alias="@type")


if TYPE_CHECKING:

    Playground.update_forward_refs()
