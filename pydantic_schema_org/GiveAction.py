from pydantic import Field
from pydantic_schema_org.Audience import Audience
from pydantic_schema_org.ContactPoint import ContactPoint
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Organization import Organization
from typing import Any, Optional, Union, List
from pydantic_schema_org.TransferAction import TransferAction


class GiveAction(TransferAction):
    """The act of transferring ownership of an object to a destination. Reciprocal of TakeAction."
     "Related actions: * [[TakeAction]]: Reciprocal of GiveAction. * [[SendAction]]: Unlike"
     "SendAction, GiveAction implies that ownership is being transferred (e.g. I may send"
     "my laptop to you, but that doesn't mean I'm giving it to you).

    See https://schema.org/GiveAction.

    """

    recipient: Optional[Union[List[Union[Audience, ContactPoint, Person, Organization]], Union[Audience, ContactPoint, Person, Organization]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    locals().update({"@type": Field("GiveAction", const=True)})


GiveAction.update_forward_refs()
