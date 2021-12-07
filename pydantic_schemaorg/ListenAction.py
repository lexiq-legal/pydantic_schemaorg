from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class ListenAction(ConsumeAction):
    """The act of consuming audio content.

    See https://schema.org/ListenAction.

    """
    type_: str = Field("ListenAction", const=True, alias='@type')
    

ListenAction.update_forward_refs()
