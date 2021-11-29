from pydantic import Field
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Audience import Audience
from pydantic_schema_org.Organization import Organization
from typing import Any, Optional, Union, List
from pydantic_schema_org.DeliveryMethod import DeliveryMethod
from pydantic_schema_org.TransferAction import TransferAction


class ReceiveAction(TransferAction):
    """The act of physically/electronically taking delivery of an object that has been transferred"
     "from an origin to a destination. Reciprocal of SendAction. Related actions: * [[SendAction]]:"
     "The reciprocal of ReceiveAction. * [[TakeAction]]: Unlike TakeAction, ReceiveAction"
     "does not imply that the ownership has been transfered (e.g. I can receive a package, but"
     "it does not mean the package is now mine).

    See https://schema.org/ReceiveAction.

    """

    sender: Optional[Union[List[Union[Person, Audience, Organization]], Union[Person, Audience, Organization]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the sending end of the action.",
    )
    deliveryMethod: Optional[Union[List[DeliveryMethod], DeliveryMethod]] = Field(
        None,
        description="A sub property of instrument. The method of delivery.",
    )
    locals().update({"@type": Field("ReceiveAction", const=True)})


ReceiveAction.update_forward_refs()
