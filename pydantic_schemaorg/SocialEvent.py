from pydantic import Field
from pydantic_schemaorg.Event import Event


class SocialEvent(Event):
    """Event type: Social event.

    See https://schema.org/SocialEvent.

    """
    type_: str = Field("SocialEvent", const=True, alias='@type')
    

SocialEvent.update_forward_refs()
