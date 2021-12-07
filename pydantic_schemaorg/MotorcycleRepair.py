from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class MotorcycleRepair(AutomotiveBusiness):
    """A motorcycle repair shop.

    See https://schema.org/MotorcycleRepair.

    """
    type_: str = Field("MotorcycleRepair", const=True, alias='@type')
    

MotorcycleRepair.update_forward_refs()
