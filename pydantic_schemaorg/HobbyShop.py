from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Store import Store


class HobbyShop(Store):
    """A store that sells materials useful or necessary for various hobbies.

    See: https://schema.org/HobbyShop
    Model depth: 5
    """

    type_: str = Field("HobbyShop", const=True, alias="@type")


if TYPE_CHECKING:

    HobbyShop.update_forward_refs()
