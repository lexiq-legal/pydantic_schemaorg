from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class HowTo(CreativeWork):
    """Instructions that explain how to achieve a result by performing a sequence of steps.

    See: https://schema.org/HowTo
    Model depth: 3
    """
    type_: str = Field("HowTo", alias='@type')
    yield_: Optional[Union[List[Union[str, 'Text', 'QuantitativeValue']], str, 'Text', 'QuantitativeValue']] = Field(
        None,alias="yield",
        description="The quantity that results by performing instructions. For example, a paper airplane,"
     "10 personalized candles.",
    )
    estimatedCost: Optional[Union[List[Union[str, 'Text', 'MonetaryAmount']], str, 'Text', 'MonetaryAmount']] = Field(
        None,
        description="The estimated cost of the supply or supplies consumed when performing instructions.",
    )
    prepTime: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        None,
        description="The length of time it takes to prepare the items to be used in instructions or a direction,"
     "in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    step: Optional[Union[List[Union[str, 'Text', 'HowToSection', 'HowToStep', 'CreativeWork']], str, 'Text', 'HowToSection', 'HowToStep', 'CreativeWork']] = Field(
        None,
        description="A single step item (as HowToStep, text, document, video, etc.) or a HowToSection.",
    )
    totalTime: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        None,
        description="The total time required to perform instructions or a direction (including time to prepare"
     "the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    performTime: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        None,
        description="The length of time it takes to perform instructions or a direction (not including time"
     "to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    tool: Optional[Union[List[Union[str, 'Text', 'HowToTool']], str, 'Text', 'HowToTool']] = Field(
        None,
        description="A sub property of instrument. An object used (but not consumed) when performing instructions"
     "or a direction.",
    )
    steps: Optional[Union[List[Union[str, 'Text', 'CreativeWork', 'ItemList']], str, 'Text', 'CreativeWork', 'ItemList']] = Field(
        None,
        description="A single step item (as HowToStep, text, document, video, etc.) or a HowToSection (originally"
     "misnamed 'steps'; 'step' is preferred).",
    )
    supply: Optional[Union[List[Union[str, 'Text', 'HowToSupply']], str, 'Text', 'HowToSupply']] = Field(
        None,
        description="A sub-property of instrument. A supply consumed when performing instructions or a direction.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.HowToSection import HowToSection
    from pydantic_schemaorg.HowToStep import HowToStep
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.HowToTool import HowToTool
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.HowToSupply import HowToSupply
