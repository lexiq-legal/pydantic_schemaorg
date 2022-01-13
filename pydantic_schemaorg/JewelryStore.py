from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class JewelryStore(Store):
    """A jewelry store.

    See: https://schema.org/JewelryStore
    Model depth: 5
    """

    type_: str = Field("JewelryStore", const=True, alias="@type")


if TYPE_CHECKING:

    JewelryStore.update_forward_refs()
