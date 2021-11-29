from pydantic import Field
from pydantic_schema_org.Action import Action


class ControlAction(Action):
    """An agent controls a device or application.

    See https://schema.org/ControlAction.

    """

    locals().update({"@type": Field("ControlAction", const=True)})


ControlAction.update_forward_refs()
