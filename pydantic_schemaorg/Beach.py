from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class Beach(CivicStructure):
    """Beach.

    See: https://schema.org/Beach
    Model depth: 4
    """

    type_: str = Field("Beach", const=True, alias="@type")


if TYPE_CHECKING:

    Beach.update_forward_refs()
