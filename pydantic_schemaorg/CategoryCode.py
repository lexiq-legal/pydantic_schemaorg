from pydantic import Field, AnyUrl
from typing import Any, Optional, Union, List
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
    inCodeSet: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="A [[CategoryCodeSet]] that contains this category code.",
    )
    

CategoryCode.update_forward_refs()
