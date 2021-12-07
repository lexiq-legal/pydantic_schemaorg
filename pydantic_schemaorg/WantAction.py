from pydantic import Field
from pydantic_schemaorg.ReactAction import ReactAction


class WantAction(ReactAction):
    """The act of expressing a desire about the object. An agent wants an object.

    See https://schema.org/WantAction.

    """
    type_: str = Field("WantAction", const=True, alias='@type')
    

WantAction.update_forward_refs()
