from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ControlAction import ControlAction


class ActivateAction(ControlAction):
    """The act of starting or activating a device or application (e.g. starting a timer or turning"
     "on a flashlight).

    See: https://schema.org/ActivateAction
    Model depth: 4
    """
    type_: str = Field("ActivateAction", alias='@type')
    

