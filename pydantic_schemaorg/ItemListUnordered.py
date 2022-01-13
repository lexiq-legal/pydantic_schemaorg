from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ItemListOrderType import ItemListOrderType


class ItemListUnordered(ItemListOrderType):
    """An ItemList ordered with no explicit order.

    See: https://schema.org/ItemListUnordered
    Model depth: 5
    """

    type_: str = Field("ItemListUnordered", const=True, alias="@type")


if TYPE_CHECKING:

    ItemListUnordered.update_forward_refs()
