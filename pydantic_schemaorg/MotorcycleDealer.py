from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class MotorcycleDealer(AutomotiveBusiness):
    """A motorcycle dealer.

    See: https://schema.org/MotorcycleDealer
    Model depth: 5
    """
    type_: str = Field("MotorcycleDealer", alias='@type')
    

