from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic import StrictBool


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Book(CreativeWork):
    """A book.

    See: https://schema.org/Book
    Model depth: 3
    """
    type_: str = Field("Book", alias='@type')
    illustrator: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        None,
        description="The illustrator of the book.",
    )
    abridged: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        None,
        description="Indicates whether the book is an abridged edition.",
    )
    isbn: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The ISBN of the book.",
    )
    numberOfPages: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        None,
        description="The number of pages in the book.",
    )
    bookFormat: Optional[Union[List[Union['BookFormatType', str]], 'BookFormatType', str]] = Field(
        None,
        description="The format of the book.",
    )
    bookEdition: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The edition of the book.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.BookFormatType import BookFormatType
