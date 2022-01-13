from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class HousePainter(HomeAndConstructionBusiness):
    """A house painting service.

    See: https://schema.org/HousePainter
    Model depth: 5
    """

    type_: str = Field("HousePainter", const=True, alias="@type")


if TYPE_CHECKING:

    HousePainter.update_forward_refs()
