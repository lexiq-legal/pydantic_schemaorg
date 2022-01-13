from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class GeneralContractor(HomeAndConstructionBusiness):
    """A general contractor.

    See: https://schema.org/GeneralContractor
    Model depth: 5
    """

    type_: str = Field("GeneralContractor", const=True, alias="@type")


if TYPE_CHECKING:

    GeneralContractor.update_forward_refs()
