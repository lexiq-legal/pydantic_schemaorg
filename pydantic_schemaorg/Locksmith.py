from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.HomeAndConstructionBusiness import HomeAndConstructionBusiness


class Locksmith(HomeAndConstructionBusiness):
    """A locksmith.

    See: https://schema.org/Locksmith
    Model depth: 5
    """

    type_: str = Field("Locksmith", const=True, alias="@type")


if TYPE_CHECKING:

    Locksmith.update_forward_refs()
