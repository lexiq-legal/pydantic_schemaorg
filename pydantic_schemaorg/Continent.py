from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Landform import Landform


class Continent(Landform):
    """One of the continents (for example, Europe or Africa).

    See: https://schema.org/Continent
    Model depth: 4
    """

    type_: str = Field("Continent", const=True, alias="@type")


if TYPE_CHECKING:

    Continent.update_forward_refs()
