from pydantic import Field
from pydantic_schemaorg.ReactAction import ReactAction


class AgreeAction(ReactAction):
    """The act of expressing a consistency of opinion with the object. An agent agrees to/about"
     "an object (a proposition, topic or theme) with participants.

    See https://schema.org/AgreeAction.

    """

    locals().update({"@type": Field("AgreeAction", const=True)})


AgreeAction.update_forward_refs()
