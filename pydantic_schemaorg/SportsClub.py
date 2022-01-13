from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class SportsClub(SportsActivityLocation):
    """A sports club.

    See: https://schema.org/SportsClub
    Model depth: 5
    """

    type_: str = Field("SportsClub", const=True, alias="@type")


if TYPE_CHECKING:

    SportsClub.update_forward_refs()
