from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.ContactPoint import ContactPoint
from typing import Any, Union, List, Optional
from pydantic_schemaorg.TransferAction import TransferAction


class GiveAction(TransferAction):
    """The act of transferring ownership of an object to a destination. Reciprocal of TakeAction."
     "Related actions: * [[TakeAction]]: Reciprocal of GiveAction. * [[SendAction]]: Unlike"
     "SendAction, GiveAction implies that ownership is being transferred (e.g. I may send"
     "my laptop to you, but that doesn't mean I'm giving it to you).

    See https://schema.org/GiveAction.

    """

    recipient: Optional[Union[List[Union[Organization, Person, Audience, ContactPoint]], Union[Organization, Person, Audience, ContactPoint]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    locals().update({"@type": Field("GiveAction", const=True)})


GiveAction.update_forward_refs()
