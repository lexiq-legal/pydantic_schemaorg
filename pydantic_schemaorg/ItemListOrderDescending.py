from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ItemListOrderType import ItemListOrderType


class ItemListOrderDescending(ItemListOrderType):
    """An ItemList ordered with higher values listed first.

    See: https://schema.org/ItemListOrderDescending
    Model depth: 5
    """

    type_: str = Field("ItemListOrderDescending", const=True, alias="@type")


if TYPE_CHECKING:

    ItemListOrderDescending.update_forward_refs()
