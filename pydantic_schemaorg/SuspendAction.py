from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ControlAction import ControlAction


class SuspendAction(ControlAction):
    """The act of momentarily pausing a device or application (e.g. pause music playback or"
     "pause a timer).

    See: https://schema.org/SuspendAction
    Model depth: 4
    """
    type_: str = Field("SuspendAction", alias='@type')
    

