from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ListItem import ListItem

from pydantic_schemaorg.ItemList import ItemList

from pydantic_schemaorg.CreativeWork import CreativeWork


class HowToStep(ListItem, ItemList, CreativeWork):
    """A step in the instructions for how to achieve a result. It is an ordered list with HowToDirection"
     "and/or HowToTip items.

    See: https://schema.org/HowToStep
    Model depth: 3
    """

    type_: str = Field("HowToStep", const=True, alias="@type")


if TYPE_CHECKING:

    HowToStep.update_forward_refs()
