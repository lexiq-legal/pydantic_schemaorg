from pydantic import AnyUrl, Field
from typing import Any, Optional, Union, List
from pydantic_schema_org.DefinedTerm import DefinedTerm


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
