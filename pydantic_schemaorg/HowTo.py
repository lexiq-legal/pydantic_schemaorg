from pydantic import Field
from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Duration import Duration
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.HowToSection import HowToSection
from pydantic_schemaorg.ItemList import ItemList


class HowTo(CreativeWork):
    """Instructions that explain how to achieve a result by performing a sequence of steps.

    See https://schema.org/HowTo.

    """

    yield_: Optional[Union[List[Union[str, QuantitativeValue]], Union[str, QuantitativeValue]]] = Field(
        None,alias="yield",
        description="The quantity that results by performing instructions. For example, a paper airplane,"
     "10 personalized candles.",
    )
    estimatedCost: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="The estimated cost of the supply or supplies consumed when performing instructions.",
    )
    prepTime: Optional[Union[List[Duration], Duration]] = Field(
        None,
        description="The length of time it takes to prepare the items to be used in instructions or a direction,"
     "in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    step: Union[List[Union[str, CreativeWork, HowToSection, Any]], Union[str, CreativeWork, HowToSection, Any]] = Field(
        None,
        description="A single step item (as HowToStep, text, document, video, etc.) or a HowToSection.",
    )
    totalTime: Optional[Union[List[Duration], Duration]] = Field(
        None,
        description="The total time required to perform instructions or a direction (including time to prepare"
     "the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    performTime: Optional[Union[List[Duration], Duration]] = Field(
        None,
        description="The length of time it takes to perform instructions or a direction (not including time"
     "to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    tool: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="A sub property of instrument. An object used (but not consumed) when performing instructions"
     "or a direction.",
    )
    steps: Optional[Union[List[Union[str, CreativeWork, ItemList]], Union[str, CreativeWork, ItemList]]] = Field(
        None,
        description="A single step item (as HowToStep, text, document, video, etc.) or a HowToSection (originally"
     "misnamed 'steps'; 'step' is preferred).",
    )
    supply: Union[List[Union[str, Any]], Union[str, Any]] = Field(
        None,
        description="A sub-property of instrument. A supply consumed when performing instructions or a direction.",
    )
    locals().update({"@type": Field("HowTo", const=True)})


HowTo.update_forward_refs()
