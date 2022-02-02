from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ControlAction import ControlAction


class ResumeAction(ControlAction):
    """The act of resuming a device or application which was formerly paused (e.g. resume music"
     "playback or resume a timer).

    See: https://schema.org/ResumeAction
    Model depth: 4
    """
    type_: str = Field("ResumeAction", alias='@type')
    

