from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Event import Event


class ChildrensEvent(Event):
    """Event type: Children's event.

    See: https://schema.org/ChildrensEvent
    Model depth: 3
    """
    type_: str = Field("ChildrensEvent", alias='@type')
    

