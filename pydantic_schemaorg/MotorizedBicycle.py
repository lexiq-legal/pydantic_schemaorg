from pydantic import Field
from pydantic_schemaorg.Vehicle import Vehicle


class MotorizedBicycle(Vehicle):
    """A motorized bicycle is a bicycle with an attached motor used to power the vehicle, or to"
     "assist with pedaling.

    See https://schema.org/MotorizedBicycle.

    """
    type_: str = Field("MotorizedBicycle", const=True, alias='@type')
    

MotorizedBicycle.update_forward_refs()
