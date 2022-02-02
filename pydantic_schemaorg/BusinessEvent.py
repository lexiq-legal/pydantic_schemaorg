from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Event import Event


class BusinessEvent(Event):
    """Event type: Business event.

    See: https://schema.org/BusinessEvent
    Model depth: 3
    """
    type_: str = Field("BusinessEvent", alias='@type')
    

