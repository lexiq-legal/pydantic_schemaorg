from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.InsertAction import InsertAction


class AppendAction(InsertAction):
    """The act of inserting at the end if an ordered collection.

    See: https://schema.org/AppendAction
    Model depth: 6
    """
    type_: str = Field(default="AppendAction", alias='@type', const=True)
    
