from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork
from pydantic_schemaorg.ListItem import ListItem
from pydantic_schemaorg.ItemList import ItemList


class HowToStep(CreativeWork, ListItem, ItemList):
    """A step in the instructions for how to achieve a result. It is an ordered list with HowToDirection"
     "and/or HowToTip items.

    See https://schema.org/HowToStep.

    """
    type_: str = Field("HowToStep", const=True, alias='@type')
    

HowToStep.update_forward_refs()
