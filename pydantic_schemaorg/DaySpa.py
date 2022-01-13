from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class DaySpa(HealthAndBeautyBusiness):
    """A day spa.

    See: https://schema.org/DaySpa
    Model depth: 5
    """

    type_: str = Field("DaySpa", const=True, alias="@type")


if TYPE_CHECKING:

    DaySpa.update_forward_refs()
