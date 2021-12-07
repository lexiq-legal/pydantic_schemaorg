from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class ReadAction(ConsumeAction):
    """The act of consuming written content.

    See https://schema.org/ReadAction.

    """
    type_: str = Field("ReadAction", const=True, alias='@type')
    

ReadAction.update_forward_refs()
