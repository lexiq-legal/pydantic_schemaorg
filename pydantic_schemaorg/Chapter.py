from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork


class Chapter(CreativeWork):
    """One of the sections into which a book is divided. A chapter usually has a section number"
     "or a name.

    See https://schema.org/Chapter.

    """

    pageStart: Optional[Union[List[Union[int, str]], Union[int, str]]] = Field(
        None,
        description="The page on which the work starts; for example \"135\" or \"xiii\".",
    )
    pagination: Optional[Union[List[str], str]] = Field(
        None,
        description="Any description of pages that is not separated into pageStart and pageEnd; for example,"
     "\"1-6, 9, 55\" or \"10-12, 46-49\".",
    )
    pageEnd: Optional[Union[List[Union[int, str]], Union[int, str]]] = Field(
        None,
        description="The page on which the work ends; for example \"138\" or \"xvi\".",
    )
    locals().update({"@type": Field("Chapter", const=True)})


Chapter.update_forward_refs()
