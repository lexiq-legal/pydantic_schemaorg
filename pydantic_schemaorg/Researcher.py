from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Audience import Audience


class Researcher(Audience):
    """Researchers.

    See: https://schema.org/Researcher
    Model depth: 4
    """

    type_: str = Field("Researcher", const=True, alias="@type")


if TYPE_CHECKING:

    Researcher.update_forward_refs()
