from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class UseAction(ConsumeAction):
    """The act of applying an object to its intended purpose.

    See https://schema.org/UseAction.

    """

    locals().update({"@type": Field("UseAction", const=True)})


UseAction.update_forward_refs()
