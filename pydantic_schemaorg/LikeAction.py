from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ReactAction import ReactAction


class LikeAction(ReactAction):
    """The act of expressing a positive sentiment about the object. An agent likes an object"
     "(a proposition, topic or theme) with participants.

    See: https://schema.org/LikeAction
    Model depth: 5
    """
    type_: str = Field("LikeAction", alias='@type')
    

