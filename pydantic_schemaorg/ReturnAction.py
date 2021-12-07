from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.ContactPoint import ContactPoint
from typing import Any, Optional, Union, List
from pydantic_schemaorg.TransferAction import TransferAction


class ReturnAction(TransferAction):
    """The act of returning to the origin that which was previously received (concrete objects)"
     "or taken (ownership).

    See https://schema.org/ReturnAction.

    """
    type_: str = Field("ReturnAction", const=True, alias='@type')
    recipient: Optional[Union[List[Union[Organization, Audience, Person, ContactPoint]], Union[Organization, Audience, Person, ContactPoint]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    

ReturnAction.update_forward_refs()
