from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class NailSalon(HealthAndBeautyBusiness):
    """A nail salon.

    See: https://schema.org/NailSalon
    Model depth: 5
    """

    type_: str = Field("NailSalon", const=True, alias="@type")


if TYPE_CHECKING:

    NailSalon.update_forward_refs()
