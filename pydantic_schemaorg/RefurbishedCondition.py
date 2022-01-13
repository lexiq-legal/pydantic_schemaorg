from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.OfferItemCondition import OfferItemCondition


class RefurbishedCondition(OfferItemCondition):
    """Indicates that the item is refurbished.

    See: https://schema.org/RefurbishedCondition
    Model depth: 5
    """

    type_: str = Field("RefurbishedCondition", const=True, alias="@type")


if TYPE_CHECKING:

    RefurbishedCondition.update_forward_refs()
