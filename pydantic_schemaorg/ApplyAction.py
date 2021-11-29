from pydantic import Field
from pydantic_schemaorg.OrganizeAction import OrganizeAction


class ApplyAction(OrganizeAction):
    """The act of registering to an organization/service without the guarantee to receive"
     "it. Related actions: * [[RegisterAction]]: Unlike RegisterAction, ApplyAction has"
     "no guarantees that the application will be accepted.

    See https://schema.org/ApplyAction.

    """

    locals().update({"@type": Field("ApplyAction", const=True)})


ApplyAction.update_forward_refs()
