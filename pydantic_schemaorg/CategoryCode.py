from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.DefinedTerm import DefinedTerm


class CategoryCode(DefinedTerm):
    """A Category Code.

    See: https://schema.org/CategoryCode
    Model depth: 4
    """

    type_: str = Field("CategoryCode", const=True, alias="@type")
    codeValue: "Optional[Union[List[str], str]]" = Field(
        None,
        description="A short textual code that uniquely identifies the value.",
    )
    inCodeSet: "Optional[Union[List[Union[AnyUrl, CategoryCodeSet, str]], Union[AnyUrl, CategoryCodeSet, str]]]" = Field(
        None,
        description="A [[CategoryCodeSet]] that contains this category code.",
    )


if TYPE_CHECKING:

    from pydantic import AnyUrl

    from pydantic_schemaorg.CategoryCodeSet import CategoryCodeSet

    CategoryCode.update_forward_refs()
