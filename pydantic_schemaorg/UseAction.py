from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class UseAction(ConsumeAction):
    """The act of applying an object to its intended purpose.

    See https://schema.org/UseAction.

    """
    type_: str = Field("UseAction", const=True, alias='@type')
    

UseAction.update_forward_refs()
