from pydantic import Field
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from decimal import Decimal
from typing import Any, Union, List, Optional
from pydantic_schemaorg.ListItem import ListItem


class HowToItem(ListItem):
    """An item used as either a tool or supply when performing the instructions for how to to achieve"
     "a result.

    See https://schema.org/HowToItem.

    """

    requiredQuantity: Optional[Union[List[Union[Decimal, str, QuantitativeValue]], Union[Decimal, str, QuantitativeValue]]] = Field(
        None,
        description="The required quantity of the item(s).",
    )
    locals().update({"@type": Field("HowToItem", const=True)})


HowToItem.update_forward_refs()
