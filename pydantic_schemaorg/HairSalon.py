from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class HairSalon(HealthAndBeautyBusiness):
    """A hair salon.

    See: https://schema.org/HairSalon
    Model depth: 5
    """

    type_: str = Field("HairSalon", const=True, alias="@type")


if TYPE_CHECKING:

    HairSalon.update_forward_refs()
