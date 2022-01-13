from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class BikeStore(Store):
    """A bike store.

    See: https://schema.org/BikeStore
    Model depth: 5
    """

    type_: str = Field("BikeStore", const=True, alias="@type")


if TYPE_CHECKING:

    BikeStore.update_forward_refs()
