from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.CreativeWork import CreativeWork


class MenuSection(CreativeWork):
    """A sub-grouping of food or drink items in a menu. E.g. courses (such as 'Dinner', 'Breakfast',"
     "etc.), specific type of dishes (such as 'Meat', 'Vegan', 'Drinks', etc.), or some other"
     "classification made by the menu provider.

    See https://schema.org/MenuSection.

    """
    type_: str = Field("MenuSection", const=True, alias='@type')
    hasMenuSection: Any = Field(
        None,
        description="A subgrouping of the menu (by dishes, course, serving time period, etc.).",
    )
    hasMenuItem: Any = Field(
        None,
        description="A food or drink item contained in a menu or menu section.",
    )
    

MenuSection.update_forward_refs()
