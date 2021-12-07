from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class MotorcycleDealer(AutomotiveBusiness):
    """A motorcycle dealer.

    See https://schema.org/MotorcycleDealer.

    """
    type_: str = Field("MotorcycleDealer", const=True, alias='@type')
    

MotorcycleDealer.update_forward_refs()
