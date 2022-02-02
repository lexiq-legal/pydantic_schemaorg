from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Vehicle import Vehicle


class MotorizedBicycle(Vehicle):
    """A motorized bicycle is a bicycle with an attached motor used to power the vehicle, or to"
     "assist with pedaling.

    See: https://schema.org/MotorizedBicycle
    Model depth: 4
    """
    type_: str = Field("MotorizedBicycle", alias='@type')
    

