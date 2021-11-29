from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class ListenAction(ConsumeAction):
    """The act of consuming audio content.

    See https://schema.org/ListenAction.

    """

    locals().update({"@type": Field("ListenAction", const=True)})


ListenAction.update_forward_refs()
