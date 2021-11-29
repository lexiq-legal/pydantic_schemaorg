from pydantic import Field
from pydantic_schemaorg.ControlAction import ControlAction


class ResumeAction(ControlAction):
    """The act of resuming a device or application which was formerly paused (e.g. resume music"
     "playback or resume a timer).

    See https://schema.org/ResumeAction.

    """

    locals().update({"@type": Field("ResumeAction", const=True)})


ResumeAction.update_forward_refs()
