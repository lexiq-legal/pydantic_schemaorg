from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class GroceryStore(Store):
    """A grocery store.

    See: https://schema.org/GroceryStore
    Model depth: 5
    """

    type_: str = Field("GroceryStore", const=True, alias="@type")


if TYPE_CHECKING:

    GroceryStore.update_forward_refs()
