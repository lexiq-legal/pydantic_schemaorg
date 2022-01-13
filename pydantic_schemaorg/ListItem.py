from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.Intangible import Intangible


class ListItem(Intangible):
    """An list item, e.g. a step in a checklist or how-to description.

    See: https://schema.org/ListItem
    Model depth: 3
    """

    type_: str = Field("ListItem", const=True, alias="@type")
    position: "Optional[Union[List[Union[int, str]], Union[int, str]]]" = Field(
        None,
        description="The position of an item in a series or sequence of items.",
    )
    nextItem: "Optional[Union[List[Union['ListItem', str]], Union['ListItem', str]]]" = Field(
        None,
        description="A link to the ListItem that follows the current one.",
    )
    previousItem: "Optional[Union[List[Union['ListItem', str]], Union['ListItem', str]]]" = Field(
        None,
        description="A link to the ListItem that preceeds the current one.",
    )
    item: "Optional[Union[List[Union[Thing, str]], Union[Thing, str]]]" = Field(
        None,
        description="An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists')’.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.Thing import Thing

    ListItem.update_forward_refs()
