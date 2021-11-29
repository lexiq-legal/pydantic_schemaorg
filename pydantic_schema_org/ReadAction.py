from pydantic import Field
from pydantic_schema_org.ConsumeAction import ConsumeAction


class ReadAction(ConsumeAction):
    """The act of consuming written content.

    See https://schema.org/ReadAction.

    """

    locals().update({"@type": Field("ReadAction", const=True)})


ReadAction.update_forward_refs()
