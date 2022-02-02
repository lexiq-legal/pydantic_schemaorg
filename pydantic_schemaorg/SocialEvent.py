from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Event import Event


class SocialEvent(Event):
    """Event type: Social event.

    See: https://schema.org/SocialEvent
    Model depth: 3
    """
    type_: str = Field("SocialEvent", alias='@type')
    

