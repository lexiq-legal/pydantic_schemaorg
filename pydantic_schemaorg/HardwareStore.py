from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class HardwareStore(Store):
    """A hardware store.

    See: https://schema.org/HardwareStore
    Model depth: 5
    """

    type_: str = Field("HardwareStore", const=True, alias="@type")


if TYPE_CHECKING:

    HardwareStore.update_forward_refs()
