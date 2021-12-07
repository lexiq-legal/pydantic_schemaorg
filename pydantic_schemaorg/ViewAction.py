from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class ViewAction(ConsumeAction):
    """The act of consuming static visual content.

    See https://schema.org/ViewAction.

    """
    type_: str = Field("ViewAction", const=True, alias='@type')
    

ViewAction.update_forward_refs()
