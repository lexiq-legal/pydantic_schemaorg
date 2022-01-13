from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class AnimalShelter(LocalBusiness):
    """Animal shelter.

    See: https://schema.org/AnimalShelter
    Model depth: 4
    """

    type_: str = Field("AnimalShelter", const=True, alias="@type")


if TYPE_CHECKING:

    AnimalShelter.update_forward_refs()
