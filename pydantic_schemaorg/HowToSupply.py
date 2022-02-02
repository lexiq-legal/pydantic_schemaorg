from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.HowToItem import HowToItem


class HowToSupply(HowToItem):
    """A supply consumed when performing the instructions for how to achieve a result.

    See: https://schema.org/HowToSupply
    Model depth: 5
    """
    type_: str = Field("HowToSupply", alias='@type')
    estimatedCost: Optional[Union[List[Union[str, 'Text', 'MonetaryAmount']], str, 'Text', 'MonetaryAmount']] = Field(
        None,
        description="The estimated cost of the supply or supplies consumed when performing instructions.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
