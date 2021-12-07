from pydantic import Field
from pydantic_schemaorg.ReactAction import ReactAction


class LikeAction(ReactAction):
    """The act of expressing a positive sentiment about the object. An agent likes an object"
     "(a proposition, topic or theme) with participants.

    See https://schema.org/LikeAction.

    """
    type_: str = Field("LikeAction", const=True, alias='@type')
    

LikeAction.update_forward_refs()
