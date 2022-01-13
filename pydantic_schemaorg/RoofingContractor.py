from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class RoofingContractor(HomeAndConstructionBusiness):
    """A roofing contractor.

    See: https://schema.org/RoofingContractor
    Model depth: 5
    """

    type_: str = Field("RoofingContractor", const=True, alias="@type")


if TYPE_CHECKING:

    RoofingContractor.update_forward_refs()
