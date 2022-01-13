from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness


class NightClub(EntertainmentBusiness):
    """A nightclub or discotheque.

    See: https://schema.org/NightClub
    Model depth: 5
    """

    type_: str = Field("NightClub", const=True, alias="@type")


if TYPE_CHECKING:

    NightClub.update_forward_refs()
