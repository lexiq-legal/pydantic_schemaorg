from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ItemList import ItemList
from pydantic_schemaorg.ListItem import ListItem
from pydantic_schemaorg.CreativeWork import CreativeWork


class HowToStep(ItemList, ListItem, CreativeWork):
    """A step in the instructions for how to achieve a result. It is an ordered list with HowToDirection"
     "and/or HowToTip items.

    See: https://schema.org/HowToStep
    Model depth: 3
    """
    type_: str = Field("HowToStep", alias='@type')
    

