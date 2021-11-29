from pydantic import Field
from pydantic_schemaorg.Message import Message


class EmailMessage(Message):
    """An email message.

    See https://schema.org/EmailMessage.

    """

    locals().update({"@type": Field("EmailMessage", const=True)})


EmailMessage.update_forward_refs()
