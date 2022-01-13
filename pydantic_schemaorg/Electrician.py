from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class Electrician(HomeAndConstructionBusiness):
    """An electrician.

    See: https://schema.org/Electrician
    Model depth: 5
    """

    type_: str = Field("Electrician", const=True, alias="@type")


if TYPE_CHECKING:

    Electrician.update_forward_refs()
