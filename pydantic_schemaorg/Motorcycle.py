from pydantic import Field
from pydantic_schemaorg.Vehicle import Vehicle


class Motorcycle(Vehicle):
    """A motorcycle or motorbike is a single-track, two-wheeled motor vehicle.

    See https://schema.org/Motorcycle.

    """
    type_: str = Field("Motorcycle", const=True, alias='@type')
    

Motorcycle.update_forward_refs()
