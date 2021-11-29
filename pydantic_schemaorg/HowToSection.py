from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.ItemList import ItemList
from typing import Any, Union, List, Optional
from pydantic_schemaorg.ListItem import ListItem


class HowToSection(CreativeWork, ItemList, ListItem):
    """A sub-grouping of steps in the instructions for how to achieve a result (e.g. steps for"
     "making a pie crust within a pie recipe).

    See https://schema.org/HowToSection.

    """

    steps: Optional[Union[List[Union[str, CreativeWork, ItemList]], Union[str, CreativeWork, ItemList]]] = Field(
        None,
        description="A single step item (as HowToStep, text, document, video, etc.) or a HowToSection (originally"
     "misnamed 'steps'; 'step' is preferred).",
    )
    locals().update({"@type": Field("HowToSection", const=True)})


HowToSection.update_forward_refs()
