from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, Optional, List
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Message(CreativeWork):
    """A single message from a sender to one or more organizations or people.

    See: https://schema.org/Message
    Model depth: 3
    """
    type_: str = Field("Message", alias='@type')
    sender: Optional[Union[List[Union['Person', 'Audience', 'Organization', str]], 'Person', 'Audience', 'Organization', str]] = Field(
        None,
        description="A sub property of participant. The participant who is at the sending end of the action.",
    )
    ccRecipient: Optional[Union[List[Union['Person', 'Organization', 'ContactPoint', str]], 'Person', 'Organization', 'ContactPoint', str]] = Field(
        None,
        description="A sub property of recipient. The recipient copied on a message.",
    )
    toRecipient: Optional[Union[List[Union['Person', 'Audience', 'Organization', 'ContactPoint', str]], 'Person', 'Audience', 'Organization', 'ContactPoint', str]] = Field(
        None,
        description="A sub property of recipient. The recipient who was directly sent the message.",
    )
    recipient: Optional[Union[List[Union['Person', 'Audience', 'Organization', 'ContactPoint', str]], 'Person', 'Audience', 'Organization', 'ContactPoint', str]] = Field(
        None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    messageAttachment: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        None,
        description="A CreativeWork attached to the message.",
    )
    dateRead: Optional[Union[List[Union[ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]], ISO8601Date, 'DateTime', ISO8601Date, 'Date', str]] = Field(
        None,
        description="The date/time at which the message has been read by the recipient if a single recipient"
     "exists.",
    )
    dateSent: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        None,
        description="The date/time at which the message was sent.",
    )
    dateReceived: Optional[Union[List[Union[ISO8601Date, 'DateTime', str]], ISO8601Date, 'DateTime', str]] = Field(
        None,
        description="The date/time the message was received if a single recipient exists.",
    )
    bccRecipient: Optional[Union[List[Union['Person', 'Organization', 'ContactPoint', str]], 'Person', 'Organization', 'ContactPoint', str]] = Field(
        None,
        description="A sub property of recipient. The recipient blind copied on a message.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
