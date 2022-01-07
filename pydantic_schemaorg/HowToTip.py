from pydantic import Field
from pydantic_schemaorg.ListItem import ListItem
from pydantic_schemaorg.CreativeWork import CreativeWork


class HowToTip(ListItem, CreativeWork):
    """An explanation in the instructions for how to achieve a result. It provides supplementary"
     "information about a technique, supply, author's preference, etc. It can explain what"
     "could be done, or what should not be done, but doesn't specify what should be done (see"
     "HowToDirection).

    See https://schema.org/HowToTip.

    """
    type_: str = Field("HowToTip", const=True, alias='@type')
    

HowToTip.update_forward_refs()
