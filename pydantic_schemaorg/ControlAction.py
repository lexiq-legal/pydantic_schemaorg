from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Action import Action


class ControlAction(Action):
    """An agent controls a device or application.

    See: https://schema.org/ControlAction
    Model depth: 3
    """
    type_: str = Field("ControlAction", alias='@type')
    

