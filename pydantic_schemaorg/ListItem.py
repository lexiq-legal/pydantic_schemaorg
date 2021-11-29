from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Thing import Thing
from pydantic_schemaorg.Intangible import Intangible


class ListItem(Intangible):
    """An list item, e.g. a step in a checklist or how-to description.

    See https://schema.org/ListItem.

    """

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
    locals().update({"@type": Field("ListItem", const=True)})


ListItem.update_forward_refs()
