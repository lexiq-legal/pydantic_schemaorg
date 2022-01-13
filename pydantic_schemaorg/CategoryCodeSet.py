from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.DefinedTermSet import DefinedTermSet


class CategoryCodeSet(DefinedTermSet):
    """A set of Category Code values.

    See: https://schema.org/CategoryCodeSet
    Model depth: 4
    """

    type_: str = Field("CategoryCodeSet", const=True, alias="@type")
    hasCategoryCode: "Optional[Union[List[Union[CategoryCode, str]], Union[CategoryCode, str]]]" = Field(
        None,
        description="A Category code contained in this code set.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.CategoryCode import CategoryCode

    CategoryCodeSet.update_forward_refs()
