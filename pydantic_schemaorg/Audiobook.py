from pydantic import Field
from pydantic_schemaorg.Duration import Duration
from typing import List, Optional, Union
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Book import Book
from pydantic_schemaorg.AudioObject import AudioObject


class Audiobook(Book, AudioObject):
    """An audiobook.

    See https://schema.org/Audiobook.

    """
    type_: str = Field("Audiobook", const=True, alias='@type')
    duration: Optional[Union[List[Union[Duration, str]], Union[Duration, str]]] = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    readBy: Optional[Union[List[Union[Person, str]], Union[Person, str]]] = Field(
        None,
        description="A person who reads (performs) the audiobook.",
    )
    

Audiobook.update_forward_refs()
