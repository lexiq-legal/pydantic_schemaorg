from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class MovingCompany(HomeAndConstructionBusiness):
    """A moving company.

    See: https://schema.org/MovingCompany
    Model depth: 5
    """

    type_: str = Field("MovingCompany", const=True, alias="@type")


if TYPE_CHECKING:

    MovingCompany.update_forward_refs()
