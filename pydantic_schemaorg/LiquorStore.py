from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class LiquorStore(Store):
    """A shop that sells alcoholic drinks such as wine, beer, whisky and other spirits.

    See: https://schema.org/LiquorStore
    Model depth: 5
    """

    type_: str = Field("LiquorStore", const=True, alias="@type")


if TYPE_CHECKING:

    LiquorStore.update_forward_refs()
