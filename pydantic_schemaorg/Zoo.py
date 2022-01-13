from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class Zoo(CivicStructure):
    """A zoo.

    See: https://schema.org/Zoo
    Model depth: 4
    """

    type_: str = Field("Zoo", const=True, alias="@type")


if TYPE_CHECKING:

    Zoo.update_forward_refs()
