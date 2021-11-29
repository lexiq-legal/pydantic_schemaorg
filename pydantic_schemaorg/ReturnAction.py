from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.ContactPoint import ContactPoint
from pydantic_schemaorg.Person import Person
from typing import List, Optional, Union, Any
from pydantic_schemaorg.TransferAction import TransferAction


class ReturnAction(TransferAction):
    """The act of returning to the origin that which was previously received (concrete objects)"
     "or taken (ownership).

    See https://schema.org/ReturnAction.

    """

    recipient: Optional[Union[List[Union[Organization, Audience, ContactPoint, Person]], Union[Organization, Audience, ContactPoint, Person]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    locals().update({"@type": Field("ReturnAction", const=True)})


ReturnAction.update_forward_refs()