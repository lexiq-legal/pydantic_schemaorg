from pydantic import Field
from pydantic_schemaorg.ContactPoint import ContactPoint
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import List, Optional, Union
from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
from pydantic_schemaorg.TransferAction import TransferAction


class SendAction(TransferAction):
    """The act of physically/electronically dispatching an object for transfer from an origin"
     "to a destination.Related actions: * [[ReceiveAction]]: The reciprocal of SendAction."
     "* [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership"
     "(e.g. I can send you my laptop, but I'm not necessarily giving it to you).

    See https://schema.org/SendAction.

    """
    type_: str = Field("SendAction", const=True, alias='@type')
    recipient: Optional[Union[List[Union[ContactPoint, Audience, Organization, Person, str]], Union[ContactPoint, Audience, Organization, Person, str]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    deliveryMethod: Optional[Union[List[Union[DeliveryMethod, str]], Union[DeliveryMethod, str]]] = Field(
        None,
        description="A sub property of instrument. The method of delivery.",
    )
    

SendAction.update_forward_refs()
