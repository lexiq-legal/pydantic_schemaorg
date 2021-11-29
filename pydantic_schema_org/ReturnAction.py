from pydantic import Field
from pydantic_schema_org.Audience import Audience
from pydantic_schema_org.ContactPoint import ContactPoint
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Organization import Organization
from typing import Any, Optional, Union, List
from pydantic_schema_org.TransferAction import TransferAction


class ReturnAction(TransferAction):
    """The act of returning to the origin that which was previously received (concrete objects)"
     "or taken (ownership).

    See https://schema.org/ReturnAction.

    """

    recipient: Optional[Union[List[Union[Audience, ContactPoint, Person, Organization]], Union[Audience, ContactPoint, Person, Organization]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    locals().update({"@type": Field("ReturnAction", const=True)})


ReturnAction.update_forward_refs()
