from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class OutletStore(Store):
    """An outlet store.

    See: https://schema.org/OutletStore
    Model depth: 5
    """

    type_: str = Field("OutletStore", const=True, alias="@type")


if TYPE_CHECKING:

    OutletStore.update_forward_refs()
