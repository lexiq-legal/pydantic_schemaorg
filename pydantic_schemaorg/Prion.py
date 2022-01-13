from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Prion(InfectiousAgentClass):
    """A prion is an infectious agent composed of protein in a misfolded form.

    See: https://schema.org/Prion
    Model depth: 6
    """

    type_: str = Field("Prion", const=True, alias="@type")


if TYPE_CHECKING:

    Prion.update_forward_refs()
