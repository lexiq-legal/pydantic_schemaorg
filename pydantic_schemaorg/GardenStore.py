from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class GardenStore(Store):
    """A garden store.

    See: https://schema.org/GardenStore
    Model depth: 5
    """

    type_: str = Field("GardenStore", const=True, alias="@type")


if TYPE_CHECKING:

    GardenStore.update_forward_refs()
