from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.HowToItem import HowToItem


class HowToSupply(HowToItem):
    """A supply consumed when performing the instructions for how to achieve a result.

    See https://schema.org/HowToSupply.

    """

    estimatedCost: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The estimated cost of the supply or supplies consumed when performing instructions.",
    )
    locals().update({"@type": Field("HowToSupply", const=True)})


HowToSupply.update_forward_refs()
