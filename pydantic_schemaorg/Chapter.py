from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Chapter(CreativeWork):
    """One of the sections into which a book is divided. A chapter usually has a section number"
     "or a name.

    See: https://schema.org/Chapter
    Model depth: 3
    """
    type_: str = Field("Chapter", alias='@type')
    pageStart: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        None,
        description="The page on which the work starts; for example \"135\" or \"xiii\".",
    )
    pagination: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="Any description of pages that is not separated into pageStart and pageEnd; for example,"
     "\"1-6, 9, 55\" or \"10-12, 46-49\".",
    )
    pageEnd: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        None,
        description="The page on which the work ends; for example \"138\" or \"xvi\".",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Text import Text
