from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class ConvenienceStore(Store):
    """A convenience store.

    See: https://schema.org/ConvenienceStore
    Model depth: 5
    """

    type_: str = Field("ConvenienceStore", const=True, alias="@type")


if TYPE_CHECKING:

    ConvenienceStore.update_forward_refs()
