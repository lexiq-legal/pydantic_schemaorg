from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class MenuSection(CreativeWork):
    """A sub-grouping of food or drink items in a menu. E.g. courses (such as 'Dinner', 'Breakfast',"
     "etc.), specific type of dishes (such as 'Meat', 'Vegan', 'Drinks', etc.), or some other"
     "classification made by the menu provider.

    See: https://schema.org/MenuSection
    Model depth: 3
    """
    type_: str = Field("MenuSection", alias='@type')
    hasMenuSection: Optional[Union[List[Union['MenuSection', str]], 'MenuSection', str]] = Field(
        None,
        description="A subgrouping of the menu (by dishes, course, serving time period, etc.).",
    )
    hasMenuItem: Optional[Union[List[Union['MenuItem', str]], 'MenuItem', str]] = Field(
        None,
        description="A food or drink item contained in a menu or menu section.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MenuItem import MenuItem
