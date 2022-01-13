from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class Bridge(CivicStructure):
    """A bridge.

    See: https://schema.org/Bridge
    Model depth: 4
    """

    type_: str = Field("Bridge", const=True, alias="@type")


if TYPE_CHECKING:

    Bridge.update_forward_refs()
