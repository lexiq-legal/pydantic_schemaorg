from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.OfferItemCondition import OfferItemCondition


class UsedCondition(OfferItemCondition):
    """Indicates that the item is used.

    See: https://schema.org/UsedCondition
    Model depth: 5
    """

    type_: str = Field("UsedCondition", const=True, alias="@type")


if TYPE_CHECKING:

    UsedCondition.update_forward_refs()
