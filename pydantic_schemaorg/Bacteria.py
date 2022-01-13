from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Bacteria(InfectiousAgentClass):
    """Pathogenic bacteria that cause bacterial infection.

    See: https://schema.org/Bacteria
    Model depth: 6
    """

    type_: str = Field("Bacteria", const=True, alias="@type")


if TYPE_CHECKING:

    Bacteria.update_forward_refs()
