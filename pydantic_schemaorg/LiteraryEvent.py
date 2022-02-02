from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Event import Event


class LiteraryEvent(Event):
    """Event type: Literary event.

    See: https://schema.org/LiteraryEvent
    Model depth: 3
    """
    type_: str = Field("LiteraryEvent", alias='@type')
    

