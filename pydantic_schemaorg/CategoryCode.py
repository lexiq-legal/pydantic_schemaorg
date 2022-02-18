from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.DefinedTerm import DefinedTerm


class CategoryCode(DefinedTerm):
    """A Category Code.

    See: https://schema.org/CategoryCode
    Model depth: 4
    """
    type_: str = Field(default="CategoryCode", alias='@type', const=True)
    codeValue: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A short textual code that uniquely identifies the value.",
    )
    inCodeSet: Optional[Union[List[Union[AnyUrl, 'URL', 'CategoryCodeSet', str]], AnyUrl, 'URL', 'CategoryCodeSet', str]] = Field(
        default=None,
        description="A [[CategoryCodeSet]] that contains this category code.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.CategoryCodeSet import CategoryCodeSet
