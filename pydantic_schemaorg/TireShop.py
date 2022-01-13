from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class TireShop(Store):
    """A tire shop.

    See: https://schema.org/TireShop
    Model depth: 5
    """

    type_: str = Field("TireShop", const=True, alias="@type")


if TYPE_CHECKING:

    TireShop.update_forward_refs()
