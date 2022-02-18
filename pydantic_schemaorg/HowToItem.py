from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.ListItem import ListItem


class HowToItem(ListItem):
    """An item used as either a tool or supply when performing the instructions for how to to achieve"
     "a result.

    See: https://schema.org/HowToItem
    Model depth: 4
    """
    type_: str = Field(default="HowToItem", alias='@type', const=True)
    requiredQuantity: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text', 'QuantitativeValue']], StrictInt, StrictFloat, 'Number', str, 'Text', 'QuantitativeValue']] = Field(
        default=None,
        description="The required quantity of the item(s).",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
