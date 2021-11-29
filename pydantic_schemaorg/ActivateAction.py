from pydantic import Field
from pydantic_schemaorg.ControlAction import ControlAction


class ActivateAction(ControlAction):
    """The act of starting or activating a device or application (e.g. starting a timer or turning"
     "on a flashlight).

    See https://schema.org/ActivateAction.

    """

    locals().update({"@type": Field("ActivateAction", const=True)})


ActivateAction.update_forward_refs()
