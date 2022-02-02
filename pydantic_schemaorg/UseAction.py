from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class UseAction(ConsumeAction):
    """The act of applying an object to its intended purpose.

    See: https://schema.org/UseAction
    Model depth: 4
    """
    type_: str = Field("UseAction", alias='@type')
    

