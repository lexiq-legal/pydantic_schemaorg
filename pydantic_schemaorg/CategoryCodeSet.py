from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.DefinedTermSet import DefinedTermSet


class CategoryCodeSet(DefinedTermSet):
    """A set of Category Code values.

    See: https://schema.org/CategoryCodeSet
    Model depth: 4
    """
    type_: str = Field("CategoryCodeSet", alias='@type')
    hasCategoryCode: Optional[Union[List[Union['CategoryCode', str]], 'CategoryCode', str]] = Field(
        None,
        description="A Category code contained in this code set.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.CategoryCode import CategoryCode
