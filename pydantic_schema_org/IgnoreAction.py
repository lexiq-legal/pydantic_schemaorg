from pydantic import Field
from pydantic_schema_org.AssessAction import AssessAction


class IgnoreAction(AssessAction):
    """The act of intentionally disregarding the object. An agent ignores an object.

    See https://schema.org/IgnoreAction.

    """

    locals().update({"@type": Field("IgnoreAction", const=True)})


IgnoreAction.update_forward_refs()
