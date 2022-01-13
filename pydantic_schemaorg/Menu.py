from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.CreativeWork import CreativeWork


class Menu(CreativeWork):
    """A structured representation of food or drink items available from a FoodEstablishment.

    See: https://schema.org/Menu
    Model depth: 3
    """

    type_: str = Field("Menu", const=True, alias="@type")
    hasMenuSection: "Optional[Union[List[Union[MenuSection, str]], Union[MenuSection, str]]]" = Field(
        None,
        description="A subgrouping of the menu (by dishes, course, serving time period, etc.).",
    )
    hasMenuItem: "Optional[Union[List[Union[MenuItem, str]], Union[MenuItem, str]]]" = (
        Field(
            None,
            description="A food or drink item contained in a menu or menu section.",
        )
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.MenuSection import MenuSection

    from pydantic_schemaorg.MenuItem import MenuItem

    Menu.update_forward_refs()
