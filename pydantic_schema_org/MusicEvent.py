from pydantic import Field
from pydantic_schema_org.Event import Event


class MusicEvent(Event):
    """Event type: Music event.

    See https://schema.org/MusicEvent.

    """

    locals().update({"@type": Field("MusicEvent", const=True)})


MusicEvent.update_forward_refs()
