from pydantic import Field
from pydantic_schemaorg.InformAction import InformAction


class ConfirmAction(InformAction):
    """The act of notifying someone that a future event/action is going to happen as expected."
     "Related actions: * [[CancelAction]]: The antonym of ConfirmAction.

    See https://schema.org/ConfirmAction.

    """

    locals().update({"@type": Field("ConfirmAction", const=True)})


ConfirmAction.update_forward_refs()
