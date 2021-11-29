from pydantic import Field
from pydantic_schema_org.Event import Event


class SocialEvent(Event):
    """Event type: Social event.

    See https://schema.org/SocialEvent.

    """

    locals().update({"@type": Field("SocialEvent", const=True)})


SocialEvent.update_forward_refs()
