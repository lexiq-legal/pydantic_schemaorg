from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Intangible import Intangible


class Quantity(Intangible):
    """Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass"
     "are entities like '3 Kg' or '4 milligrams'.

    See: https://schema.org/Quantity
    Model depth: 3
    """

    type_: str = Field("Quantity", const=True, alias="@type")


if TYPE_CHECKING:

    Quantity.update_forward_refs()
