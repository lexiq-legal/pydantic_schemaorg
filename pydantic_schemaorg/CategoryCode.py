from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.DefinedTerm import DefinedTerm


class CategoryCode(DefinedTerm):
    """A Category Code.

    See: https://schema.org/CategoryCode
    Model depth: 4
    """
    type_: str = Field("CategoryCode", alias='@type')
    codeValue: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="A short textual code that uniquely identifies the value.",
    )
    inCodeSet: Optional[Union[List[Union[AnyUrl, 'URL', 'CategoryCodeSet', str]], AnyUrl, 'URL', 'CategoryCodeSet', str]] = Field(
        None,
        description="A [[CategoryCodeSet]] that contains this category code.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.CategoryCodeSet import CategoryCodeSet
