from pydantic import Field
from pydantic_schemaorg.Audience import Audience
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import List, Optional, Union
from pydantic_schemaorg.ContactPoint import ContactPoint
from pydantic_schemaorg.CreativeWork import CreativeWork
from datetime import datetime, date


class Message(CreativeWork):
    """A single message from a sender to one or more organizations or people.

    See https://schema.org/Message.

    """
    type_: str = Field("Message", const=True, alias='@type')
    sender: Optional[Union[List[Union[Audience, Organization, Person, str]], Union[Audience, Organization, Person, str]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the sending end of the action.",
    )
    ccRecipient: Optional[Union[List[Union[ContactPoint, Organization, Person, str]], Union[ContactPoint, Organization, Person, str]]] = Field(
        None,
        description="A sub property of recipient. The recipient copied on a message.",
    )
    toRecipient: Optional[Union[List[Union[ContactPoint, Audience, Organization, Person, str]], Union[ContactPoint, Audience, Organization, Person, str]]] = Field(
        None,
        description="A sub property of recipient. The recipient who was directly sent the message.",
    )
    recipient: Optional[Union[List[Union[ContactPoint, Audience, Organization, Person, str]], Union[ContactPoint, Audience, Organization, Person, str]]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    messageAttachment: Optional[Union[List[Union[CreativeWork, str]], Union[CreativeWork, str]]] = Field(
        None,
        description="A CreativeWork attached to the message.",
    )
    dateRead: Optional[Union[List[Union[datetime, date, str]], Union[datetime, date, str]]] = Field(
        None,
        description="The date/time at which the message has been read by the recipient if a single recipient"
     "exists.",
    )
    dateSent: Optional[Union[List[Union[datetime, str]], Union[datetime, str]]] = Field(
        None,
        description="The date/time at which the message was sent.",
    )
    dateReceived: Optional[Union[List[Union[datetime, str]], Union[datetime, str]]] = Field(
        None,
        description="The date/time the message was received if a single recipient exists.",
    )
    bccRecipient: Optional[Union[List[Union[ContactPoint, Organization, Person, str]], Union[ContactPoint, Organization, Person, str]]] = Field(
        None,
        description="A sub property of recipient. The recipient blind copied on a message.",
    )
    

Message.update_forward_refs()
