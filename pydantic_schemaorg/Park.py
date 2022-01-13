from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class Park(CivicStructure):
    """A park.

    See: https://schema.org/Park
    Model depth: 4
    """

    type_: str = Field("Park", const=True, alias="@type")


if TYPE_CHECKING:

    Park.update_forward_refs()
