from pydantic import Field
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Audience import Audience
from pydantic_schema_org.Organization import Organization
from typing import Any, Optional, Union, List
from pydantic_schema_org.CreativeWork import CreativeWork
from datetime import datetime, date


class Message(CreativeWork):
    """A single message from a sender to one or more organizations or people.

    See https://schema.org/Message.

    """

    sender: Optional[Union[List[Union[Person, Audience, Organization]], Union[Person, Audience, Organization]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the sending end of the action.",
    )
    ccRecipient: Union[List[Union[Person, Organization, Any]], Union[Person, Organization, Any]] = Field(
        None,
        description="A sub property of recipient. The recipient copied on a message.",
    )
    toRecipient: Union[List[Union[Audience, Person, Organization, Any]], Union[Audience, Person, Organization, Any]] = Field(
        None,
        description="A sub property of recipient. The recipient who was directly sent the message.",
    )
    recipient: Union[List[Union[Audience, Person, Organization, Any]], Union[Audience, Person, Organization, Any]] = Field(
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
    bccRecipient: Union[List[Union[Person, Organization, Any]], Union[Person, Organization, Any]] = Field(
        None,
        description="A sub property of recipient. The recipient blind copied on a message.",
    )
    locals().update({"@type": Field("Message", const=True)})


Message.update_forward_refs()
