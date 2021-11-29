from pydantic import Field, StrictBool
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.BookFormatType import BookFormatType
from pydantic_schemaorg.CreativeWork import CreativeWork


class Book(CreativeWork):
    """A book.

    See https://schema.org/Book.

    """

    illustrator: Optional[Union[List[Person], Person]] = Field(
        None,
        description="The illustrator of the book.",
    )
    abridged: Optional[Union[List[StrictBool], StrictBool]] = Field(
        None,
        description="Indicates whether the book is an abridged edition.",
    )
    isbn: Optional[Union[List[str], str]] = Field(
        None,
        description="The ISBN of the book.",
    )
    numberOfPages: Optional[Union[List[int], int]] = Field(
        None,
        description="The number of pages in the book.",
    )
    bookFormat: Optional[Union[List[BookFormatType], BookFormatType]] = Field(
        None,
        description="The format of the book.",
    )
    bookEdition: Optional[Union[List[str], str]] = Field(
        None,
        description="The edition of the book.",
    )
    locals().update({"@type": Field("Book", const=True)})


Book.update_forward_refs()
