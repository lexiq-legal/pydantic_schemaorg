from pydantic import Field
from pydantic_schemaorg.Event import Event


class MusicEvent(Event):
    """Event type: Music event.

    See https://schema.org/MusicEvent.

    """
    type_: str = Field("MusicEvent", const=True, alias='@type')
    

MusicEvent.update_forward_refs()
