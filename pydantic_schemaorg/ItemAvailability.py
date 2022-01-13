from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class ItemAvailability(Enumeration):
    """A list of possible product availability options.

    See: https://schema.org/ItemAvailability
    Model depth: 4
    """

    type_: str = Field("ItemAvailability", const=True, alias="@type")


if TYPE_CHECKING:

    ItemAvailability.update_forward_refs()
