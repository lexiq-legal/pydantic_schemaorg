from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Event import Event


class MusicEvent(Event):
    """Event type: Music event.

    See: https://schema.org/MusicEvent
    Model depth: 3
    """
    type_: str = Field("MusicEvent", alias='@type')
    

