from pydantic import AnyUrl, Field
from typing import List, Optional, Union
from pydantic_schemaorg.CategoryCodeSet import CategoryCodeSet
from pydantic_schemaorg.DefinedTerm import DefinedTerm


class CategoryCode(DefinedTerm):
    """A Category Code.

    See https://schema.org/CategoryCode.

    """
    type_: str = Field("CategoryCode", const=True, alias='@type')
    codeValue: Optional[Union[List[str], str]] = Field(
        None,
        description="A short textual code that uniquely identifies the value.",
    )
    inCodeSet: Optional[Union[List[Union[AnyUrl, CategoryCodeSet, str]], Union[AnyUrl, CategoryCodeSet, str]]] = Field(
        None,
        description="A [[CategoryCodeSet]] that contains this category code.",
    )
    

CategoryCode.update_forward_refs()
