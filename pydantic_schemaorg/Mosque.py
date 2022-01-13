from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.PlaceOfWorship import PlaceOfWorship


class Mosque(PlaceOfWorship):
    """A mosque.

    See: https://schema.org/Mosque
    Model depth: 5
    """

    type_: str = Field("Mosque", const=True, alias="@type")


if TYPE_CHECKING:

    Mosque.update_forward_refs()
