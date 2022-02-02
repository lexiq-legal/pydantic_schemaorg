from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class AutoRental(AutomotiveBusiness):
    """A car rental business.

    See: https://schema.org/AutoRental
    Model depth: 5
    """
    type_: str = Field("AutoRental", alias='@type')
    

