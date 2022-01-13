from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Message import Message


class EmailMessage(Message):
    """An email message.

    See: https://schema.org/EmailMessage
    Model depth: 4
    """

    type_: str = Field("EmailMessage", const=True, alias="@type")


if TYPE_CHECKING:

    EmailMessage.update_forward_refs()
