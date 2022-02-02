from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Conversation(CreativeWork):
    """One or more messages between organizations or people on a particular topic. Individual"
     "messages can be linked to the conversation with isPartOf or hasPart properties.

    See: https://schema.org/Conversation
    Model depth: 3
    """
    type_: str = Field("Conversation", alias='@type')
    

