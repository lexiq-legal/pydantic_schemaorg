from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Audience import Audience
from typing import Any, Union, List, Optional
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

    sender: Optional[Union[List[Union[Organization, Person, Audience]], Union[Organization, Person, Audience]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the sending end of the action.",
    )
    deliveryMethod: Optional[Union[List[DeliveryMethod], DeliveryMethod]] = Field(
        None,
        description="A sub property of instrument. The method of delivery.",
    )
    locals().update({"@type": Field("ReceiveAction", const=True)})


ReceiveAction.update_forward_refs()
