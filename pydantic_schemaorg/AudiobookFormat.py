from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.BookFormatType import BookFormatType


class AudiobookFormat(BookFormatType):
    """Book format: Audiobook. This is an enumerated value for use with the bookFormat property."
     "There is also a type 'Audiobook' in the bib extension which includes Audiobook specific"
     "properties.

    See: https://schema.org/AudiobookFormat
    Model depth: 5
    """
    type_: str = Field("AudiobookFormat", alias='@type')
    

