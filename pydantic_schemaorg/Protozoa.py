from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.InfectiousAgentClass import InfectiousAgentClass


class Protozoa(InfectiousAgentClass):
    """Single-celled organism that causes an infection.

    See: https://schema.org/Protozoa
    Model depth: 6
    """

    type_: str = Field("Protozoa", const=True, alias="@type")


if TYPE_CHECKING:

    Protozoa.update_forward_refs()
