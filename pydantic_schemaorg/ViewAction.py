from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class ViewAction(ConsumeAction):
    """The act of consuming static visual content.

    See: https://schema.org/ViewAction
    Model depth: 4
    """
    type_: str = Field("ViewAction", alias='@type')
    

