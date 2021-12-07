from pydantic import Field
from pydantic_schemaorg.UseAction import UseAction


class WearAction(UseAction):
    """The act of dressing oneself in clothing.

    See https://schema.org/WearAction.

    """
    type_: str = Field("WearAction", const=True, alias='@type')
    

WearAction.update_forward_refs()
