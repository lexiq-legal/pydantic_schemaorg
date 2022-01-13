from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class PerformingArtsTheater(CivicStructure):
    """A theater or other performing art center.

    See: https://schema.org/PerformingArtsTheater
    Model depth: 4
    """

    type_: str = Field("PerformingArtsTheater", const=True, alias="@type")


if TYPE_CHECKING:

    PerformingArtsTheater.update_forward_refs()
