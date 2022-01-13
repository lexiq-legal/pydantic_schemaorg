from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class MulticellularParasite(InfectiousAgentClass):
    """Multicellular parasite that causes an infection.

    See: https://schema.org/MulticellularParasite
    Model depth: 6
    """

    type_: str = Field("MulticellularParasite", const=True, alias="@type")


if TYPE_CHECKING:

    MulticellularParasite.update_forward_refs()
