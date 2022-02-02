from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Event import Event


class Festival(Event):
    """Event type: Festival.

    See: https://schema.org/Festival
    Model depth: 3
    """
    type_: str = Field("Festival", alias='@type')
    

