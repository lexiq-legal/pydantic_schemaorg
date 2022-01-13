from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.LocalBusiness import LocalBusiness


class Store(LocalBusiness):
    """A retail good store.

    See: https://schema.org/Store
    Model depth: 4
    """

    type_: str = Field("Store", const=True, alias="@type")


if TYPE_CHECKING:

    Store.update_forward_refs()
