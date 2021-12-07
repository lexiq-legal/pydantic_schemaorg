from pydantic import Field
from pydantic_schemaorg.Action import Action


class InteractAction(Action):
    """The act of interacting with another person or organization.

    See https://schema.org/InteractAction.

    """
    type_: str = Field("InteractAction", const=True, alias='@type')
    

InteractAction.update_forward_refs()
