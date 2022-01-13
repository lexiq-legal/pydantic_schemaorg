from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Enumeration import Enumeration


class OfferItemCondition(Enumeration):
    """A list of possible conditions for the item.

    See: https://schema.org/OfferItemCondition
    Model depth: 4
    """

    type_: str = Field("OfferItemCondition", const=True, alias="@type")


if TYPE_CHECKING:

    OfferItemCondition.update_forward_refs()
