from pydantic import Field
from pydantic_schemaorg.Message import Message


class EmailMessage(Message):
    """An email message.

    See https://schema.org/EmailMessage.

    """
    type_: str = Field("EmailMessage", const=True, alias='@type')
    

EmailMessage.update_forward_refs()
