from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class GasStation(AutomotiveBusiness):
    """A gas station.

    See: https://schema.org/GasStation
    Model depth: 5
    """
    type_: str = Field("GasStation", alias='@type')
    

