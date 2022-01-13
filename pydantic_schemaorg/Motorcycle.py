from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Vehicle import Vehicle


class Motorcycle(Vehicle):
    """A motorcycle or motorbike is a single-track, two-wheeled motor vehicle.

    See: https://schema.org/Motorcycle
    Model depth: 4
    """

    type_: str = Field("Motorcycle", const=True, alias="@type")


if TYPE_CHECKING:

    Motorcycle.update_forward_refs()
