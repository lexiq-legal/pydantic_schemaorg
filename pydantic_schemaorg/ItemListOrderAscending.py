from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ItemListOrderType import ItemListOrderType


class ItemListOrderAscending(ItemListOrderType):
    """An ItemList ordered with lower values listed first.

    See: https://schema.org/ItemListOrderAscending
    Model depth: 5
    """

    type_: str = Field("ItemListOrderAscending", const=True, alias="@type")


if TYPE_CHECKING:

    ItemListOrderAscending.update_forward_refs()
