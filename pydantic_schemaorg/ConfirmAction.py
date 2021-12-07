from pydantic import Field
from pydantic_schemaorg.InformAction import InformAction


class ConfirmAction(InformAction):
    """The act of notifying someone that a future event/action is going to happen as expected."
     "Related actions: * [[CancelAction]]: The antonym of ConfirmAction.

    See https://schema.org/ConfirmAction.

    """
    type_: str = Field("ConfirmAction", const=True, alias='@type')
    

ConfirmAction.update_forward_refs()
