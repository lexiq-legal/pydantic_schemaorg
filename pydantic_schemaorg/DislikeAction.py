from pydantic import Field
from pydantic_schemaorg.ReactAction import ReactAction


class DislikeAction(ReactAction):
    """The act of expressing a negative sentiment about the object. An agent dislikes an object"
     "(a proposition, topic or theme) with participants.

    See https://schema.org/DislikeAction.

    """

    locals().update({"@type": Field("DislikeAction", const=True)})


DislikeAction.update_forward_refs()
