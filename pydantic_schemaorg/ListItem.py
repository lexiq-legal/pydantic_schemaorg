from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Intangible import Intangible


class ListItem(Intangible):
    """An list item, e.g. a step in a checklist or how-to description.

    See https://schema.org/ListItem.

    """
    type_: str = Field("ListItem", const=True, alias='@type')
    position: Optional[Union[List[Union[int, str]], Union[int, str]]] = Field(
        None,
        description="The position of an item in a series or sequence of items.",
    )
    nextItem: Any = Field(
        None,
        description="A link to the ListItem that follows the current one.",
    )
    previousItem: Any = Field(
        None,
        description="A link to the ListItem that preceeds the current one.",
    )
    item: Optional[Union[List[Thing], Thing]] = Field(
        None,
        description="An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists')’.",
    )
    

ListItem.update_forward_refs()
