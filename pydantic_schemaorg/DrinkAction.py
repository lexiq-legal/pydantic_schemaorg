from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class DrinkAction(ConsumeAction):
    """The act of swallowing liquids.

    See https://schema.org/DrinkAction.

    """
    type_: str = Field("DrinkAction", const=True, alias='@type')
    

DrinkAction.update_forward_refs()
