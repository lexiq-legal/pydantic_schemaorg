from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class SportingGoodsStore(Store):
    """A sporting goods store.

    See: https://schema.org/SportingGoodsStore
    Model depth: 5
    """

    type_: str = Field("SportingGoodsStore", const=True, alias="@type")


if TYPE_CHECKING:

    SportingGoodsStore.update_forward_refs()
