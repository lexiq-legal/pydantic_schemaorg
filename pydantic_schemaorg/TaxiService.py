from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Service import Service


class TaxiService(Service):
    """A service for a vehicle for hire with a driver for local travel. Fares are usually calculated"
     "based on distance traveled.

    See: https://schema.org/TaxiService
    Model depth: 4
    """
    type_: str = Field("TaxiService", alias='@type')
    

