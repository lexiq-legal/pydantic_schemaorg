from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class HealthAndBeautyBusiness(LocalBusiness):
    """Health and beauty.

    See: https://schema.org/HealthAndBeautyBusiness
    Model depth: 4
    """

    type_: str = Field("HealthAndBeautyBusiness", const=True, alias="@type")


if TYPE_CHECKING:

    HealthAndBeautyBusiness.update_forward_refs()
