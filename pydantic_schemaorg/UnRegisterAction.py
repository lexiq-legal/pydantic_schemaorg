from pydantic import Field
from pydantic_schemaorg.InteractAction import InteractAction


class UnRegisterAction(InteractAction):
    """The act of un-registering from a service. Related actions: * [[RegisterAction]]: antonym"
     "of UnRegisterAction. * [[LeaveAction]]: Unlike LeaveAction, UnRegisterAction implies"
     "that you are unregistering from a service you werer previously registered, rather than"
     "leaving a team/group of people.

    See https://schema.org/UnRegisterAction.

    """
    type_: str = Field("UnRegisterAction", const=True, alias='@type')
    

UnRegisterAction.update_forward_refs()
