from pydantic import Field
from pydantic_schemaorg.AssessAction import AssessAction


class IgnoreAction(AssessAction):
    """The act of intentionally disregarding the object. An agent ignores an object.

    See https://schema.org/IgnoreAction.

    """
    type_: str = Field("IgnoreAction", const=True, alias='@type')
    

IgnoreAction.update_forward_refs()
