from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.DefinedTerm import DefinedTerm


class CategoryCode(DefinedTerm):
    """A Category Code.

    See https://schema.org/CategoryCode.

    """

    codeValue: Optional[Union[List[str], str]] = Field(
        None,
        description="A short textual code that uniquely identifies the value.",
    )
    inCodeSet: Union[List[Union[AnyUrl, Any]], Union[AnyUrl, Any]] = Field(
        None,
        description="A [[CategoryCodeSet]] that contains this category code.",
    )
    locals().update({"@type": Field("CategoryCode", const=True)})


CategoryCode.update_forward_refs()
