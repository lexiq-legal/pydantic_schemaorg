from pydantic import Field
from pydantic_schemaorg.Action import Action


class AssessAction(Action):
    """The act of forming one's opinion, reaction or sentiment.

    See https://schema.org/AssessAction.

    """
    type_: str = Field("AssessAction", const=True, alias='@type')
    

AssessAction.update_forward_refs()
