from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Person import Person
from typing import Any, Optional, Union, List
from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
from pydantic_schemaorg.TransferAction import TransferAction


class ReceiveAction(TransferAction):
    """The act of physically/electronically taking delivery of an object that has been transferred"
     "from an origin to a destination. Reciprocal of SendAction. Related actions: * [[SendAction]]:"
     "The reciprocal of ReceiveAction. * [[TakeAction]]: Unlike TakeAction, ReceiveAction"
     "does not imply that the ownership has been transfered (e.g. I can receive a package, but"
     "it does not mean the package is now mine).

    See https://schema.org/ReceiveAction.

    """
    type_: str = Field("ReceiveAction", const=True, alias='@type')
    sender: Optional[Union[List[Union[Organization, Audience, Person]], Union[Organization, Audience, Person]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the sending end of the action.",
    )
    deliveryMethod: Optional[Union[List[DeliveryMethod], DeliveryMethod]] = Field(
        None,
        description="A sub property of instrument. The method of delivery.",
    )
    

ReceiveAction.update_forward_refs()
