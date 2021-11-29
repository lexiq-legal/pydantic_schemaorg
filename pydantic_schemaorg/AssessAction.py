from pydantic import Field
from pydantic_schemaorg.Action import Action


class AssessAction(Action):
    """The act of forming one's opinion, reaction or sentiment.

    See https://schema.org/AssessAction.

    """

    locals().update({"@type": Field("AssessAction", const=True)})


AssessAction.update_forward_refs()
