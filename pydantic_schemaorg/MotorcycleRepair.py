from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class MotorcycleRepair(AutomotiveBusiness):
    """A motorcycle repair shop.

    See: https://schema.org/MotorcycleRepair
    Model depth: 5
    """
    type_: str = Field("MotorcycleRepair", alias='@type')
    

