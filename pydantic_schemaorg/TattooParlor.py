from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HealthAndBeautyBusiness import HealthAndBeautyBusiness


class TattooParlor(HealthAndBeautyBusiness):
    """A tattoo parlor.

    See: https://schema.org/TattooParlor
    Model depth: 5
    """

    type_: str = Field("TattooParlor", const=True, alias="@type")


if TYPE_CHECKING:

    TattooParlor.update_forward_refs()
