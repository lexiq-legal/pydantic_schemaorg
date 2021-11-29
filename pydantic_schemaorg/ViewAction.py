from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class ViewAction(ConsumeAction):
    """The act of consuming static visual content.

    See https://schema.org/ViewAction.

    """

    locals().update({"@type": Field("ViewAction", const=True)})


ViewAction.update_forward_refs()
