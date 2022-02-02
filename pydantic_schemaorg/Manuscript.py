from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Manuscript(CreativeWork):
    """A book, document, or piece of music written by hand rather than typed or printed.

    See: https://schema.org/Manuscript
    Model depth: 3
    """
    type_: str = Field("Manuscript", alias='@type')
    

