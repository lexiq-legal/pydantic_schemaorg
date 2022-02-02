from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Service import Service


class Taxi(Service):
    """A taxi.

    See: https://schema.org/Taxi
    Model depth: 4
    """
    type_: str = Field("Taxi", alias='@type')
    

