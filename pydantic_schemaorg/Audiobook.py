from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.AudioObject import AudioObject
from pydantic_schemaorg.Book import Book


class Audiobook(AudioObject, Book):
    """An audiobook.

    See https://schema.org/Audiobook.

    """
    type_: str = Field("Audiobook", const=True, alias='@type')
    duration: Any = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    readBy: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A person who reads (performs) the audiobook.",
    )
    

Audiobook.update_forward_refs()
