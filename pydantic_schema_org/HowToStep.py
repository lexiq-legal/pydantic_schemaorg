from pydantic import Field
from pydantic_schema_org.CreativeWork import CreativeWork
from pydantic_schema_org.ListItem import ListItem
from pydantic_schema_org.ItemList import ItemList


class HowToStep(CreativeWork, ListItem, ItemList):
    """A step in the instructions for how to achieve a result. It is an ordered list with HowToDirection"
     "and/or HowToTip items.

    See https://schema.org/HowToStep.

    """

    locals().update({"@type": Field("HowToStep", const=True)})


HowToStep.update_forward_refs()
