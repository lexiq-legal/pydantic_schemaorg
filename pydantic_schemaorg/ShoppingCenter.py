from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class ShoppingCenter(LocalBusiness):
    """A shopping center or mall.

    See: https://schema.org/ShoppingCenter
    Model depth: 4
    """

    type_: str = Field("ShoppingCenter", const=True, alias="@type")


if TYPE_CHECKING:

    ShoppingCenter.update_forward_refs()
