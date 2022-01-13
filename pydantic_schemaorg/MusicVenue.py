from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class MusicVenue(CivicStructure):
    """A music venue.

    See: https://schema.org/MusicVenue
    Model depth: 4
    """

    type_: str = Field("MusicVenue", const=True, alias="@type")


if TYPE_CHECKING:

    MusicVenue.update_forward_refs()
