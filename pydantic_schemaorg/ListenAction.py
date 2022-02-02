from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class ListenAction(ConsumeAction):
    """The act of consuming audio content.

    See: https://schema.org/ListenAction
    Model depth: 4
    """
    type_: str = Field("ListenAction", alias='@type')
    

