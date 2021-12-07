from pydantic import Field
from pydantic_schemaorg.AutomotiveBusiness import AutomotiveBusiness


class GasStation(AutomotiveBusiness):
    """A gas station.

    See https://schema.org/GasStation.

    """
    type_: str = Field("GasStation", const=True, alias='@type')
    

GasStation.update_forward_refs()
