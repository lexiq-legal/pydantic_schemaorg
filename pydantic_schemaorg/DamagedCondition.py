from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.OfferItemCondition import OfferItemCondition


class DamagedCondition(OfferItemCondition):
    """Indicates that the item is damaged.

    See: https://schema.org/DamagedCondition
    Model depth: 5
    """

    type_: str = Field("DamagedCondition", const=True, alias="@type")


if TYPE_CHECKING:

    DamagedCondition.update_forward_refs()
