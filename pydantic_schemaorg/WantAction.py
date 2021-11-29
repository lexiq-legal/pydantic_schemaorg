from pydantic import Field
from pydantic_schemaorg.ReactAction import ReactAction


class WantAction(ReactAction):
    """The act of expressing a desire about the object. An agent wants an object.

    See https://schema.org/WantAction.

    """

    locals().update({"@type": Field("WantAction", const=True)})


WantAction.update_forward_refs()
