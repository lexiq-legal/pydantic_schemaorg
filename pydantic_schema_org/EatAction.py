from pydantic import Field
from pydantic_schema_org.ConsumeAction import ConsumeAction


class EatAction(ConsumeAction):
    """The act of swallowing solid objects.

    See https://schema.org/EatAction.

    """

    locals().update({"@type": Field("EatAction", const=True)})


EatAction.update_forward_refs()
