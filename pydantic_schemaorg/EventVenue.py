from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CivicStructure import CivicStructure


class EventVenue(CivicStructure):
    """An event venue.

    See: https://schema.org/EventVenue
    Model depth: 4
    """

    type_: str = Field("EventVenue", const=True, alias="@type")


if TYPE_CHECKING:

    EventVenue.update_forward_refs()
