from pydantic import Field
from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
from typing import List, Optional, Union
from pydantic_schemaorg.HowToItem import HowToItem


class HowToSupply(HowToItem):
    """A supply consumed when performing the instructions for how to achieve a result.

    See https://schema.org/HowToSupply.

    """
    type_: str = Field("HowToSupply", const=True, alias='@type')
    estimatedCost: Optional[Union[List[Union[str, MonetaryAmount]], Union[str, MonetaryAmount]]] = Field(
        None,
        description="The estimated cost of the supply or supplies consumed when performing instructions.",
    )
    

HowToSupply.update_forward_refs()
