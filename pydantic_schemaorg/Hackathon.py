from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Event import Event


class Hackathon(Event):
    """A [hackathon](https://en.wikipedia.org/wiki/Hackathon) event.

    See: https://schema.org/Hackathon
    Model depth: 3
    """
    type_: str = Field("Hackathon", alias='@type')
    

