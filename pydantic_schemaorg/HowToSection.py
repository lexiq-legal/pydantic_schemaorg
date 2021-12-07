from pydantic import Field
from pydantic_schemaorg.ItemList import ItemList
from pydantic_schemaorg.CreativeWork import CreativeWork
from typing import Any, Optional, Union, List
from pydantic_schemaorg.ListItem import ListItem


class HowToSection(CreativeWork, ListItem, ItemList):
    """A sub-grouping of steps in the instructions for how to achieve a result (e.g. steps for"
     "making a pie crust within a pie recipe).

    See https://schema.org/HowToSection.

    """
    type_: str = Field("HowToSection", const=True, alias='@type')
    steps: Optional[Union[List[Union[str, ItemList, CreativeWork]], Union[str, ItemList, CreativeWork]]] = Field(
        None,
        description="A single step item (as HowToStep, text, document, video, etc.) or a HowToSection (originally"
     "misnamed 'steps'; 'step' is preferred).",
    )
    

HowToSection.update_forward_refs()
