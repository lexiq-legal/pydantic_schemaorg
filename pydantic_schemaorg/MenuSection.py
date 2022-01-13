from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.CreativeWork import CreativeWork


class MenuSection(CreativeWork):
    """A sub-grouping of food or drink items in a menu. E.g. courses (such as 'Dinner', 'Breakfast',"
     "etc.), specific type of dishes (such as 'Meat', 'Vegan', 'Drinks', etc.), or some other"
     "classification made by the menu provider.

    See: https://schema.org/MenuSection
    Model depth: 3
    """

    type_: str = Field("MenuSection", const=True, alias="@type")
    hasMenuSection: "Optional[Union[List[Union['MenuSection', str]], Union['MenuSection', str]]]" = Field(
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

    from pydantic_schemaorg.MenuItem import MenuItem

    MenuSection.update_forward_refs()
