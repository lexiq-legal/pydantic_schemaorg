from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class ReadAction(ConsumeAction):
    """The act of consuming written content.

    See: https://schema.org/ReadAction
    Model depth: 4
    """
    type_: str = Field("ReadAction", alias='@type')
    

