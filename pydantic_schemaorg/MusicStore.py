from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class MusicStore(Store):
    """A music store.

    See: https://schema.org/MusicStore
    Model depth: 5
    """

    type_: str = Field("MusicStore", const=True, alias="@type")


if TYPE_CHECKING:

    MusicStore.update_forward_refs()
