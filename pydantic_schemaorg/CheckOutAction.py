from pydantic import Field
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class CheckOutAction(CommunicateAction):
    """The act of an agent communicating (service provider, social media, etc) their departure"
     "of a previously reserved service (e.g. flight check in) or place (e.g. hotel). Related"
     "actions: * [[CheckInAction]]: The antonym of CheckOutAction. * [[DepartAction]]:"
     "Unlike DepartAction, CheckOutAction implies that the agent is informing/confirming"
     "the end of a previously reserved service. * [[CancelAction]]: Unlike CancelAction,"
     "CheckOutAction implies that the agent is informing/confirming the end of a previously"
     "reserved service.

    See https://schema.org/CheckOutAction.

    """

    locals().update({"@type": Field("CheckOutAction", const=True)})


CheckOutAction.update_forward_refs()
