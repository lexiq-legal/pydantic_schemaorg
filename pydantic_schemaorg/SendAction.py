from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Audience import Audience
from typing import Any, Union, List, Optional
from pydantic_schemaorg.TransferAction import TransferAction


class SendAction(TransferAction):
    """The act of physically/electronically dispatching an object for transfer from an origin"
     "to a destination.Related actions: * [[ReceiveAction]]: The reciprocal of SendAction."
     "* [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership"
     "(e.g. I can send you my laptop, but I'm not necessarily giving it to you).

    See https://schema.org/SendAction.

    """

    recipient: Union[List[Union[Organization, Person, Audience, Any]], Union[Organization, Person, Audience, Any]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    deliveryMethod: Any = Field(
        None,
        description="A sub property of instrument. The method of delivery.",
    )
    locals().update({"@type": Field("SendAction", const=True)})


SendAction.update_forward_refs()
