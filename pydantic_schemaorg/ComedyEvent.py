from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Event import Event


class ComedyEvent(Event):
    """Event type: Comedy event.

    See: https://schema.org/ComedyEvent
    Model depth: 3
    """
    type_: str = Field("ComedyEvent", alias='@type')
    

