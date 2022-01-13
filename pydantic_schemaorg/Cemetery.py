from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class Cemetery(CivicStructure):
    """A graveyard.

    See: https://schema.org/Cemetery
    Model depth: 4
    """

    type_: str = Field("Cemetery", const=True, alias="@type")


if TYPE_CHECKING:

    Cemetery.update_forward_refs()
