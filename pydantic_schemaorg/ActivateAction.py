from pydantic import Field
from pydantic_schemaorg.ControlAction import ControlAction


class ActivateAction(ControlAction):
    """The act of starting or activating a device or application (e.g. starting a timer or turning"
     "on a flashlight).

    See https://schema.org/ActivateAction.

    """
    type_: str = Field("ActivateAction", const=True, alias='@type')
    

ActivateAction.update_forward_refs()
