from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.InformAction import InformAction


class ConfirmAction(InformAction):
    """The act of notifying someone that a future event/action is going to happen as expected."
     "Related actions: * [[CancelAction]]: The antonym of ConfirmAction.

    See: https://schema.org/ConfirmAction
    Model depth: 6
    """
    type_: str = Field("ConfirmAction", alias='@type')
    

