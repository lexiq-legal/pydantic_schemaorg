from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class ComputerStore(Store):
    """A computer store.

    See: https://schema.org/ComputerStore
    Model depth: 5
    """

    type_: str = Field("ComputerStore", const=True, alias="@type")


if TYPE_CHECKING:

    ComputerStore.update_forward_refs()
