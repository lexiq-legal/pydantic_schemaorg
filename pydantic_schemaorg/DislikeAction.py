from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ReactAction import ReactAction


class DislikeAction(ReactAction):
    """The act of expressing a negative sentiment about the object. An agent dislikes an object"
     "(a proposition, topic or theme) with participants.

    See: https://schema.org/DislikeAction
    Model depth: 5
    """
    type_: str = Field("DislikeAction", alias='@type')
    

