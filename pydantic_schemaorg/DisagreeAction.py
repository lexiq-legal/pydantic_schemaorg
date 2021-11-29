from pydantic import Field
from pydantic_schemaorg.ReactAction import ReactAction


class DisagreeAction(ReactAction):
    """The act of expressing a difference of opinion with the object. An agent disagrees to/about"
     "an object (a proposition, topic or theme) with participants.

    See https://schema.org/DisagreeAction.

    """

    locals().update({"@type": Field("DisagreeAction", const=True)})


DisagreeAction.update_forward_refs()
