from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class EatAction(ConsumeAction):
    """The act of swallowing solid objects.

    See https://schema.org/EatAction.

    """
    type_: str = Field("EatAction", const=True, alias='@type')
    

EatAction.update_forward_refs()
