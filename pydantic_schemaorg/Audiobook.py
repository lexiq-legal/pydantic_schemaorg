from pydantic import Field
from typing import List, Optional, Union, Any
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.AudioObject import AudioObject
from pydantic_schemaorg.Book import Book


class Audiobook(AudioObject, Book):
    """An audiobook.

    See https://schema.org/Audiobook.

    """

    duration: Any = Field(
        None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    readBy: Optional[Union[List[Person], Person]] = Field(
        None,
        description="A person who reads (performs) the audiobook.",
    )
    locals().update({"@type": Field("Audiobook", const=True)})


Audiobook.update_forward_refs()
