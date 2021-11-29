from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Person import Person
from typing import List, Optional, Union, Any
from pydantic_schemaorg.CreativeWork import CreativeWork
from datetime import date, datetime


class Message(CreativeWork):
    """A single message from a sender to one or more organizations or people.

    See https://schema.org/Message.

    """

    sender: Optional[Union[List[Union[Organization, Audience, Person]], Union[Organization, Audience, Person]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the sending end of the action.",
    )
    ccRecipient: Union[List[Union[Organization, Person, Any]], Union[Organization, Person, Any]] = Field(
        None,
        description="A sub property of recipient. The recipient copied on a message.",
    )
    toRecipient: Union[List[Union[Audience, Organization, Person, Any]], Union[Audience, Organization, Person, Any]] = Field(
        None,
        description="A sub property of recipient. The recipient who was directly sent the message.",
    )
    recipient: Union[List[Union[Organization, Audience, Person, Any]], Union[Organization, Audience, Person, Any]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    messageAttachment: Optional[Union[List[CreativeWork], CreativeWork]] = Field(
        None,
        description="A CreativeWork attached to the message.",
    )
    dateRead: Optional[Union[List[Union[datetime, date]], Union[datetime, date]]] = Field(
        None,
        description="The date/time at which the message has been read by the recipient if a single recipient"
     "exists.",
    )
    dateSent: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The date/time at which the message was sent.",
    )
    dateReceived: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The date/time the message was received if a single recipient exists.",
    )
    bccRecipient: Union[List[Union[Organization, Person, Any]], Union[Organization, Person, Any]] = Field(
        None,
        description="A sub property of recipient. The recipient blind copied on a message.",
    )
    locals().update({"@type": Field("Message", const=True)})


Message.update_forward_refs()
