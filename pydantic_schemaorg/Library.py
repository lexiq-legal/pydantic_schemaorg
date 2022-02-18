from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class Library(LocalBusiness):
    """A library.

    See: https://schema.org/Library
    Model depth: 4
    """
    type_: str = Field(default="Library", alias='@type', const=True)
    
