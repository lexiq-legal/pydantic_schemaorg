from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class FurnitureStore(Store):
    """A furniture store.

    See: https://schema.org/FurnitureStore
    Model depth: 5
    """

    type_: str = Field("FurnitureStore", const=True, alias="@type")


if TYPE_CHECKING:

    FurnitureStore.update_forward_refs()
