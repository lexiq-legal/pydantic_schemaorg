from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class HomeGoodsStore(Store):
    """A home goods store.

    See: https://schema.org/HomeGoodsStore
    Model depth: 5
    """

    type_: str = Field("HomeGoodsStore", const=True, alias="@type")


if TYPE_CHECKING:

    HomeGoodsStore.update_forward_refs()
