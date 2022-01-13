from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness

from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation


class HealthClub(HealthAndBeautyBusiness, SportsActivityLocation):
    """A health club.

    See: https://schema.org/HealthClub
    Model depth: 5
    """

    type_: str = Field("HealthClub", const=True, alias="@type")


if TYPE_CHECKING:

    HealthClub.update_forward_refs()
