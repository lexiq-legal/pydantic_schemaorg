from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Virus(InfectiousAgentClass):
    """Pathogenic virus that causes viral infection.

    See: https://schema.org/Virus
    Model depth: 6
    """

    type_: str = Field("Virus", const=True, alias="@type")


if TYPE_CHECKING:

    Virus.update_forward_refs()
