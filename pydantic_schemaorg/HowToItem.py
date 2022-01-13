from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.ListItem import ListItem


class HowToItem(ListItem):
    """An item used as either a tool or supply when performing the instructions for how to to achieve"
     "a result.

    See: https://schema.org/HowToItem
    Model depth: 4
    """

    type_: str = Field("HowToItem", const=True, alias="@type")
    requiredQuantity: "Optional[Union[List[Union[Decimal, str, QuantitativeValue]], Union[Decimal, str, QuantitativeValue]]]" = Field(
        None,
        description="The required quantity of the item(s).",
    )


if TYPE_CHECKING:

    from decimal import Decimal

    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue

    HowToItem.update_forward_refs()
