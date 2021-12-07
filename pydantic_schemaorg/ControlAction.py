from pydantic import Field
from pydantic_schemaorg.Action import Action


class ControlAction(Action):
    """An agent controls a device or application.

    See https://schema.org/ControlAction.

    """
    type_: str = Field("ControlAction", const=True, alias='@type')
    

ControlAction.update_forward_refs()
