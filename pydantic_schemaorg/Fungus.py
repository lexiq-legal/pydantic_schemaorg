from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Fungus(InfectiousAgentClass):
    """Pathogenic fungus.

    See: https://schema.org/Fungus
    Model depth: 6
    """

    type_: str = Field("Fungus", const=True, alias="@type")


if TYPE_CHECKING:

    Fungus.update_forward_refs()
