from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class ComedyClub(EntertainmentBusiness):
    """A comedy club.

    See: https://schema.org/ComedyClub
    Model depth: 5
    """

    type_: str = Field("ComedyClub", const=True, alias="@type")


if TYPE_CHECKING:

    ComedyClub.update_forward_refs()
