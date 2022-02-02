from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.InsertAction import InsertAction


class PrependAction(InsertAction):
    """The act of inserting at the beginning if an ordered collection.

    See: https://schema.org/PrependAction
    Model depth: 6
    """
    type_: str = Field("PrependAction", alias='@type')
    

