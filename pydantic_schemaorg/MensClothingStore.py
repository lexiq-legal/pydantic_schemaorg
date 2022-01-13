from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class MensClothingStore(Store):
    """A men's clothing store.

    See: https://schema.org/MensClothingStore
    Model depth: 5
    """

    type_: str = Field("MensClothingStore", const=True, alias="@type")


if TYPE_CHECKING:

    MensClothingStore.update_forward_refs()
